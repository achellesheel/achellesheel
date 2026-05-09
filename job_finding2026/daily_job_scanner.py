import time
import datetime
import csv
import re
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from textblob import TextBlob

# ==========================================================
# CONFIGURATION - FILL THIS IN BEFORE RUNNING
# ==========================================================
LINKEDIN_EMAIL = "YOUR_EMAIL_HERE"
LINKEDIN_PASSWORD = "YOUR_PASSWORD_HERE"

# Search Parameters
# Broader keywords to capture more jobs
SEARCH_KEYWORD = '"AI research" OR "Machine Learning" OR "Deep Learning" OR "NLP"'
SEARCH_LOCATION = "Bangalore"

# Semantic Filtering Parameters
TARGET_AI_KEYWORDS = "Artificial Intelligence Machine Learning Deep Learning NLP Natural Language Processing Agentic AI LLM Generative AI Neural Networks"
SEMANTIC_THRESHOLD = 0.05 # Minimum similarity score to be considered relevant

# ==========================================================
# LOAD PRE-TRAINED ML MODELS
# ==========================================================
print("Loading ML models...")
try:
    tfidf = joblib.load("tfidf.pkl")
    svm = joblib.load("svm_model.pkl")
    xgb = joblib.load("xgb_model.pkl")
except Exception as e:
    print("Error loading models. Did you run the main training script first?")
    exit()

# Helper features from main script
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def grammar_score(text):
    text_str = str(text)
    excessive_punct = len(re.findall(r'[!?]{2,}', text_str))
    all_caps = len(re.findall(r'\b[A-Z]{3,}\b', text_str))
    return excessive_punct + all_caps

def has_scam_keywords(text):
    wfh_keywords = ['work from home', 'easy money', 'quick cash', 'earn money fast', 'no experience']
    text = str(text).lower()
    for kw in wfh_keywords:
        if kw in text: return 1
    return 0

def predict_fake(title, company, description, is_remote):
    combined = clean_text(f"{title} {company} {description}")
    text_vector = tfidf.transform([combined])
    
    scam_kw = has_scam_keywords(description)
    grammar = grammar_score(description)
    telecommuting = 1 if is_remote else 0
    has_company_logo = 1
    has_questions = 0
    salary_num = 0
    salary_flag = 0

    from scipy.sparse import hstack
    structured = np.array([[scam_kw, grammar, telecommuting, has_company_logo, has_questions, salary_num, salary_flag]])
    final_input = hstack([text_vector, structured])

    svm_p = svm.predict_proba(final_input)[0][1]
    xgb_p = xgb.predict_proba(final_input)[0][1]
    final_prob = (svm_p * 0.4) + (xgb_p * 0.6)
    
    return final_prob

def get_semantic_score(description):
    # Use the loaded TF-IDF vectorizer to convert text to mathematical vectors
    desc_clean = clean_text(description)
    target_clean = clean_text(TARGET_AI_KEYWORDS)
    
    # We must transform both using the exact same vocabulary as the trained model
    desc_vector = tfidf.transform([desc_clean])
    target_vector = tfidf.transform([target_clean])
    
    # Calculate Cosine Similarity
    score = cosine_similarity(desc_vector, target_vector)[0][0]
    return score

# ==========================================================
# SELENIUM SCRAPING LOGIC
# ==========================================================
print("Starting Chrome...")
import os
options = webdriver.ChromeOptions()

# Create a folder in the current directory to save the Chrome profile
profile_path = os.path.join(os.getcwd(), "linkedin_chrome_profile")
options.add_argument(f"user-data-dir={profile_path}") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 1. Login to LinkedIn (with session reuse)
    print("Checking login status...")
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(5)
    
    if "login" in driver.current_url or "checkpoint" in driver.current_url or "feed" not in driver.current_url:
        print("You are not logged in.")
        print("Please log in manually in the Chrome window that just opened.")
        print("You have 90 seconds to solve any captchas and log in...")
        
        try:
            # Attempt to auto-fill the form to help out
            driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
            driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
        except:
            pass # Form might be different, let user do it manually
            
        # Wait until URL changes to feed (user successfully logged in)
        try:
            WebDriverWait(driver, 90).until(EC.url_contains("feed"))
            print("Successfully logged in! Chrome will remember this session for next time.")
        except:
            print("Timed out waiting for login. Will attempt to proceed anyway, but it might fail.")
    else:
        print("Already logged in! Reusing saved Chrome session.")
        
    # 2. Search for Jobs (Last 24 Hours, Entry Level/Internship)
    print(f"Searching for '{SEARCH_KEYWORD}' in '{SEARCH_LOCATION}' (Last 24 Hours, Entry Level/Intern)...")
    # f_TPR=r86400 (Past 24 Hours), f_E=1,2 (Internship, Entry level)
    # distance=80 (80km), f_WT=1,2,3 (On-site, Remote, Hybrid)
    search_url = f"https://www.linkedin.com/jobs/search/?keywords={SEARCH_KEYWORD.replace(' ', '%20')}&location={SEARCH_LOCATION.replace(' ', '%20')}&f_TPR=r86400&f_E=1,2&distance=80&f_WT=1,2,3"
    driver.get(search_url)
    time.sleep(5)
    
    # 3. Extract Jobs
    print("Loading up to 100 jobs...")
    time.sleep(5) 
    
    # Scroll down the left panel to load more jobs
    for _ in range(15): # Increased scroll attempts to reach 100
        try:
            cards = driver.find_elements(By.CSS_SELECTOR, ".job-card-container, li.jobs-search-results__list-item")
            if len(cards) > 0:
                driver.execute_script("arguments[0].scrollIntoView(true);", cards[-1])
            time.sleep(2)
            if len(cards) >= 100:
                break
        except:
            pass

    job_cards = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")
    if not job_cards:
        job_cards = driver.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
        
    job_count = min(len(job_cards), 100)
    print(f"Found {job_count} job cards on the screen.")
    
    results = []
    
    for i in range(job_count):
        try:
            # Re-fetch cards to prevent "stale element reference" errors as DOM changes
            current_cards = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")
            if not current_cards:
                current_cards = driver.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
                
            if i >= len(current_cards):
                break # Reached the end unexpectedly
                
            card = current_cards[i]
            
            # Click card to load description on the right panel
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
            time.sleep(1)
            card.click()
            time.sleep(3)
            
            # Extract basic info (using broader search within the card)
            title_elem = card.find_element(By.CSS_SELECTOR, "a.job-card-list__title, strong, .artdeco-entity-lockup__title")
            title = title_elem.text
            
            # Find the actual job link
            try:
                # Most reliable way: Look for any link containing '/jobs/view/'
                link_elem = card.find_element(By.CSS_SELECTOR, "a[href*='/jobs/view/']")
                link = link_elem.get_attribute("href")
            except:
                try:
                    # Fallback: Just grab the first link we can find in the card
                    link_elem = card.find_element(By.TAG_NAME, "a")
                    link = link_elem.get_attribute("href")
                except:
                    link = "No Link"
            
            try:
                company = card.find_element(By.CSS_SELECTOR, ".job-card-container__primary-description, .artdeco-entity-lockup__subtitle").text
            except:
                company = "Unknown Company"
            
            # Try to get description from the right panel
            try:
                desc_element = driver.find_element(By.ID, "job-details")
                description = desc_element.text
            except:
                description = ""
                
            # 4. Semantic Filtering
            semantic_score = get_semantic_score(description)
            if semantic_score < SEMANTIC_THRESHOLD:
                print(f"Skipped [{i+1}/5]: {title} (Low AI Relevance: {semantic_score:.3f})")
                continue
                
            is_remote = "remote" in title.lower() or "remote" in SEARCH_LOCATION.lower()
            
            # 5. Predict Fake/Real
            prob = predict_fake(title, company, description, is_remote)
            
            status = "SAFE"
            if prob > 0.7: status = "HIGH RISK"
            elif prob > 0.4: status = "SUSPICIOUS"
            
            print(f"Found [{i+1}/{len(job_cards)}]: {title} at {company} -> {status} (Fake Prob: {prob:.2f}, AI Relevance: {semantic_score:.3f})")
            
            results.append([title, company, status, f"{prob:.2f}", f"{semantic_score:.3f}", link])
            
        except Exception as e:
            print(f"Skipped job #{i+1} due to error: {str(e)[:100]}...")
            continue

    # 6. Save to CSV
    date_str = datetime.datetime.now().strftime("%d_%m_%Y")
    filename = f"finding_job_{date_str}.csv"
    
    headers = ["Job Title", "Company", "Status", "Fraud Probability", "AI Relevance Score", "Link"]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(results)
        
    print(f"\n✅ Finished! Results saved to {filename}")
    
    # 7. Print Table to Terminal
    if len(results) > 0:
        print("\n" + "="*90)
        print("FINAL JOB REPORT (PAST 24 HOURS)")
        print("="*90)
        df_out = pd.DataFrame(results, columns=headers)
        # Drop link column from terminal print so it's readable
        df_print = df_out.drop(columns=["Link"])
        print(df_print.to_string(index=False))
        print("="*90)
    else:
        print("\nNo jobs matched your criteria in the past 24 hours.")

except Exception as e:
    print(f"Critical Error: {e}")
finally:
    driver.quit()
