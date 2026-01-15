import os

UPLOAD_FOLDER = "../data/uploads/"

def process_video(file):
    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # ---- Replace this with real AI processing ----
    # Example metrics structure
    metrics = {
        "player_movements": 15,  # Number of players tracked
        "tactics": 3,            # Number of patterns detected
        "performance": 7         # Number of performance metrics
    }

    return {
        "filename": file.filename,
        "status": "Success",
        "metrics": metrics
    }
