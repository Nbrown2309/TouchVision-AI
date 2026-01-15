from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        file = request.files['video']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            # Placeholder: call AI analysis function
            metrics = {"message": "Video uploaded successfully! Processing soon."}
            return render_template('results.html', results=metrics)
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
