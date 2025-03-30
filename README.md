# Comicfy - AI-Driven Comic Creator 🎨🤖
> **Transform your text into dynamic comic panels using generative AI!**

This project leverages state-of-the-art AI technologies, including Stable Diffusion and Natural Language Processing (NLP), to create comic panels from a user-provided script. The intuitive interface and seamless backend integration allow users to generate stunning visual narratives in seconds.

---

## 🚀 Features
- **Converts user-input scripts into visually compelling comic panels.**
- **Automatically parses scripts into individual scenes using NLP techniques.**
- **Dynamically generates corresponding images for each scene with Stable Diffusion.**
- **Fully customizable pipeline for text-to-image generation.**

---

## 📂 Directory Structure
Below is the hierarchy of the project directory:

```
📦 AI-Driven Comic Creator
├── backend/                     # Backend logic
│   ├── app.py                   # Flask application
│   ├── comic_generator.py       # Stable Diffusion integration
│   ├── nlp_parser.py            # NLP script parser
│   ├── requirements.txt         # Python dependencies
│   └── assets/                  # Generated assets
│       ├── sample_scripts/      # Example scripts for testing
│       └── generated_panels/    # Generated comic panels
├── frontend/                    # Frontend logic
│   ├── index.html               # Main HTML file
│   ├── styles.css               # Styling for the web interface
│   ├── script.js                # Client-side JavaScript logic
├── datasets/                    # Dataset files
│   ├── preprocesses_data/       # Preprocessed data for training
│   └── training_data/           # Training data for Stable Diffusion or other models
```

---

## 💻 Installation and Usage
Follow these steps to clone the repository and set up the project on your local system:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/comicfy.git
   cd comicfy
   ```

2. **Set Up the Backend**
    *Navigate to the `backend/` directory*: 
   ```bash
   cd backend
   ```
    *Install Python dependencies*: 
   ```bash
   pip install -r requirements.txt
   ```
    *Download the Stable Diffusion model weights (use your preferred provider or Hugging Face)*:
   ```bash
   python -m diffusers.pipelines.stable_diffusion.download --model runwayml/stable-diffusion-v1-5
   ```
    *Run the Flask server*: 
   ```bash
   python app.py
   ```

3. **Set Up the Frontend**
    *Open the `index.html` file in your browser*:
   ```bash
   frontend/index.html
   ```

4. **Test the Application**:
   
    *Input your comic script in the text box and click "Generate Comic"*.
    *Generated comic panels will appear dynamically on the page and be saved in the `backend/assets/generated_panels/` directory*.

---

## 🔧 Dependencies
Listed in `requirements.txt`:
- `torch==2.0.1+cu118`         # PyTorch for model integration
- `diffusers==0.16.1`          # Stable Diffusion pipeline
- `transformers==4.30.0`       # Hugging Face Transformers for NLP
- `spacy==3.5.0`               # NLP script parsing
- `Pillow==9.4.0`              # Image processing (speech bubbles, layout)
- `opencv-python`              # Panel layout optimization
- `numpy==1.24.0`              # Numerical computations
- `flask==3.0.3`               # Backend framework for serving the application
- `Werkzeug==3.0.3`

---

## 💉 Requirements
Make sure the following are installed on your system:
- `Python 3.8+` 
- `pip` (Python package manager)
- A `CUDA` enabled GPU (for faster image generation)
  
---

## 🪛 How It Works
- **Input Script**: The user inputs a script describing the comic's scenes in natural language.
- **NLP Parsing**: The backend parses the script into individual scenes using NLP techniques (`nlp_parser.py`).
- **Image Generation**: Each scene is passed to Stable Diffusion to create an image (`comic_generator.py`).
- **Frontend Display**: The generated panels are displayed dynamically on the webpage.
  
---
## 📜 Future Enhancements
-It's still a work in progress with just the frontend remaining.
- Embed demonstration videos and sample images of generated comic panels.
- API endpoints for third-party integrations.

---

## 📧 Contact
For queries or feedback, reach out at [pragyavijay20318@gmail.com].

---
