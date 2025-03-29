from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import send_from_directory
import os
from comic_generator import generate_image, initialize_pipeline
from nlp_parser import parse_script
# Initialize the pipeline globally
pipeline = initialize_pipeline()

app = Flask(__name__)
CORS(app)

@app.route('/generate_comic', methods=['POST'])
def generate_comic():
    try:
        data = request.json
        print("Received request:", data)

        script = data.get("script")
        if not script:
            return jsonify({"error": "Script is missing!"}), 400

        parsed_script = parse_script(script)
        print("Parsed script:", parsed_script) 

        output_images = []
        output_dir = "./assets/generated_panels/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")

        for i, scene in enumerate(parsed_script):
            output_path = f"./assets/generated_panels/panel_{i + 1}.png"
            print(f"Generating panel {i + 1} with text: {scene['text']}")
            generate_image(scene["text"], output_path, pipeline)  # Pass the pipeline
            output_images.append(output_path)

        return jsonify({"images": output_images})

    except Exception as e:
        error_message = f"An error occurred: {e}\n{traceback.format_exc()}"
        print(error_message)
        return jsonify({"error": error_message}), 500
    
@app.route('/assets/<path:path>')
def serve_assets(path):
    return send_from_directory('assets', path)

if __name__ == "__main__":
    app.run(debug=True)
