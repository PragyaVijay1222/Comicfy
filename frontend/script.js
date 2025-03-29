document.getElementById("scriptForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const scriptInput = document.getElementById("scriptInput").value;
    if (!scriptInput) {
        alert("Please enter a script!");
        return;
    }

    try {
        // Send the script to the backend
        const response = await fetch("http://127.0.0.1:5000/generate_comic", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ script: scriptInput })
        });

        if (!response.ok) {
            throw new Error("Failed to generate comic");
        }

        const data = await response.json();

        // Display generated panels
        const panelContainer = document.getElementById("panelContainer") || document.createElement("div");
        if (!document.getElementById("panelContainer")) {
            panelContainer.id = "panelContainer";
            document.body.appendChild(panelContainer); // Append only if it doesn't exist
        }

        // Clear previous panels
        panelContainer.innerHTML = "";

        data.images.forEach(imagePath => {
            const imgElement = document.createElement("img");
            imgElement.src = `http://127.0.0.1:5000/assets/generated_panels/${imagePath.split('/').pop()}`;
            imgElement.alt = "Comic Panel";
            imgElement.className = "comic-panel";
            panelContainer.appendChild(imgElement);
        });

    } catch (error) {
        console.error(error);
        alert("An error occurred while generating the comic");
    }
});