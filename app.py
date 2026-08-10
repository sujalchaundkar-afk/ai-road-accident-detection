from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Folder where uploaded accident images will be stored
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Get uploaded image
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

        # Save the image
        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            image.filename
        )

        image.save(file_path)

        # Prototype analysis
        # This will be replaced with the actual AI model later
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
    app.run(debug=True)
