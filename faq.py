from transformers import AutoTokenizer, AutoModel
import torch
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# Load the pre-trained model and tokenizer
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)

# Load FAQ data
with open("data.json", "r") as f:
    faq_data = json.load(f)

# Pre-compute embeddings for FAQ questions
def compute_embeddings(questions):
    inputs = tokenizer(questions, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

faq_questions = [item["question"] for item in faq_data]
faq_answers = [item["answer"] for item in faq_data]
faq_embeddings = compute_embeddings(faq_questions)

# Function to find the best matching FAQ
def find_best_match(query):
    query_embedding = compute_embeddings([query])
    scores = torch.nn.functional.cosine_similarity(query_embedding, faq_embeddings)
    best_match_idx = torch.argmax(scores).item()
    return faq_answers[best_match_idx], scores[best_match_idx].item()

# Flask app
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route("/faq", methods=["POST"])
def faq():
    user_query = request.json.get("query")
    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    answer, confidence = find_best_match(user_query)
    return jsonify({"query": user_query, "answer": answer, "confidence": confidence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
