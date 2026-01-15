from flask import Flask, render_template, request, send_from_directory
from services import process_video
import os

UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route("/")
def upload_page():
    return render_template("upload.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["video"]
    result = process_video(file)
    return render_template("results.html", result=result)

# Serve uploaded videos
@app.route("/data/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
