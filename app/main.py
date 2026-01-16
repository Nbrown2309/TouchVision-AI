from flask import Flask, render_template, request
from services import process_video

app = Flask(__name__)

@app.route("/")
def upload_page():
    return render_template("upload.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("video")

    if not file or file.filename == "":
        return render_template(
            "results.html",
            result=None,
            error="No video file uploaded."
        )

    result = process_video(file)

    if result is None:
        return render_template(
            "results.html",
            result=None,
            error="Video processing failed."
        )

    return render_template(
        "results.html",
        result=result,
        error=None
    )

if __name__ == "__main__":
    app.run(debug=True)
