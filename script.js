const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const analyzeBtn = document.getElementById("analyzeBtn");

const loading = document.getElementById("loading");
const resultCard = document.getElementById("resultCard");

const accidentStatus = document.getElementById("accidentStatus");
const severity = document.getElementById("severity");
const locationText = document.getElementById("location");
const emergency = document.getElementById("emergency");
const message = document.getElementById("message");


// Show image preview
imageInput.addEventListener("change", function () {

    const file = imageInput.files[0];

    if (file) {
        const imageURL = URL.createObjectURL(file);

        previewImage.src = imageURL;
        previewImage.style.display = "block";
    }
});


// Analyze image
analyzeBtn.addEventListener("click", async function () {

    const file = imageInput.files[0];

    if (!file) {
        alert("Please upload an accident image first.");
        return;
    }

    const formData = new FormData();

    formData.append("image", file);

    loading.style.display = "block";
    resultCard.style.display = "none";

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.success) {

            accidentStatus.textContent =
                data.accident_detected ? "Accident Detected" : "No Accident Detected";

            severity.textContent = data.severity;

            locationText.textContent = data.location;

            emergency.textContent = data.emergency;

            message.textContent = data.message;

            resultCard.style.display = "block";

        } else {

            alert(data.message);

        }

    } catch (error) {

        console.log(error);

        alert(
            "Unable to connect to the server. Please make sure the Flask application is running."
        );

    }

    loading.style.display = "none";
});
