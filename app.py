from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Main page
@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# Serve CSS file
@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")


# Serve JavaScript file
@app.route("/script.js")
def javascript():
    return send_from_directory(".", "script.js")


# Analyze uploaded image
@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        if "image" not in request.files:
            return jsonify({
                "success": False,
                "message": "Please upload an image."
            })

        image = request.files["image"]

        if image.filename == "":
            return jsonify({
                "success": False,
                "message": "No image selected."
            })

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            image.filename
        )

        image.save(file_path)

        # Simple prototype analysis
        result = {
            "success": True,
            "accident_detected": True,
            "severity": "High",
            "location": "Location detected from device",
            "emergency": "Emergency response recommended",
            "message": "Possible road accident detected. Emergency assistance may be required."
        }

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "success": False,
            "message": "Something went wrong.",
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
