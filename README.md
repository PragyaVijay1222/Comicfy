# Comicfy - AI-Driven Comic Creator 🎨🤖

Comicfy is an innovative application that leverages generative AI techniques and NLP to transform small stories into visually engaging comic panels. By combining state-of-the-art text-to-image generation models and layout optimization tools, Comicfy delivers an end-to-end comic creation experience.

---

## 🚀 Features
- **Story-to-Comic Conversion**: Generate multiple comic panels based on user-provided story chunks.
- **NLP-Powered Text Parsing**: Automatically break down user stories into meaningful segments using SpaCy.
- **Image Generation**: Create high-quality images with Diffusers and the Stable Diffusion model.
- **Speech Bubble Integration**: Add dialogue or captions to panels seamlessly.
- **Panel Layout Optimization**: Arrange panels for a fluid storytelling experience.

---

## 📂 Directory Structure
Below is the hierarchy of the project directory:

```
Comicfy/
├── README.md               # Project documentation
├── requirements.txt        # Dependencies
├── frontend/               # Frontend files
│   ├── index.html          # HTML structure
│   ├── style.css           # Styling
│   └── script.js           # JavaScript logic
├── backend/                # Backend files
│   ├── app.py              # Flask application
│   ├── assets/             # Static assets like images or models
│   ├── comic_generator.py  # Core image generation logic
│   ├── nlp_parser.py       # Story segmentation
│   ├── panel_layout.py     # Panel arrangement logic
│   ├── speech_bubbles.py   # Speech bubble placement
│   └── utils.py            # Utility scripts
├── datasets/               # Dataset files
│   ├── preprocesses_data/  # Preprocessed data for training
│   └── training_data/      # Training data for Stable Diffusion or other models
```

---

## 💻 Installation and Usage
Follow these steps to clone the repository and set up the project on your local system:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/comicfy.git
   cd comicfy
   ```

2. **Create a Virtual Environment** (Optional but Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Make sure you have Python 3.8+ and GPU CUDA support. Run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Pretrained Models**:
   Place the `runwayml/stable-diffusion-v1-5` model files in the `backend/assets` directory. Update paths in `comic_generator.py` as needed.

5. **Run the Backend**:
   Start the Flask app:
   ```bash
   python backend/app.py
   ```

6. **Run the Frontend**:
   Open `frontend/index.html` in your browser or host it locally.

7. **Test the Workflow**:
   - Input a small story into the frontend interface.
   - The NLP parser will segment the story.
   - The Comic Generator will create images based on the parsed chunks.
   - Speech bubbles and panels will be finalized for download.

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

Ensure a CUDA-enabled GPU for optimal performance.

---

## 📜 Future Enhancements
-It's still a work in progress with just the frontend remaining.
- Embed demonstration videos and sample images of generated comic panels.
- API endpoints for third-party integrations.

---

## 📧 Contact
For queries or feedback, reach out at [pragyavijay20318@gmail.com].

---
