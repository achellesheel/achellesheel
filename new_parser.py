from flask import Flask, render_template, request, redirect, url_for
import os
from typing import List

app = Flask(__name__)

# Import your resume parsing functions here
from resume import parse_resume  # Replace with the actual script name

skill_keywords = ['Python', 'Java', 'SQL', 'Machine Learning', 'AWS', 'Docker']

@app.route("/")
def index():
    return render_template("upload.html")  # Upload form

@app.route("/upload", methods=["POST"])
def upload():
    if "resume" not in request.files:
        return "No file part", 400
    file = request.files["resume"]
    if file.filename == "":
        return "No selected file", 400

    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Parse the uploaded resume
    parsed_data = parse_resume(file_path, skill_keywords)

    return render_template("resume.html", data=parsed_data)

if __name__ == "__main__":
    app.run(debug=True)
