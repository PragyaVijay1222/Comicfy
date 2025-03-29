import spacy
import os

spacy.require_gpu()  # Use GPU for faster NLP processing

def parse_script(script_or_text):
    # Load the SpaCy model
    nlp = spacy.load("en_core_web_sm")
    parsed_data = []

    # Check if the input is a file path
    if os.path.exists(script_or_text):
        with open(script_or_text, 'r') as file:
            script = file.read()
    else:
        # Treat the input as raw text
        script = script_or_text

    # Process the script using SpaCy
    doc = nlp(script)

    # Parse sentences and entities
    for sent in doc.sents:
        parsed_data.append({"text": sent.text, "entities": [{"text": ent.text, "label": ent.label_} for ent in sent.ents]})

    return parsed_data

if __name__ == "__main__":
    # For testing, you can use either a file path or raw text
    # Example 1: File path input
    script_path = "./assets/sample_scripts/comic_script.txt"
    if os.path.exists(script_path):
        data = parse_script(script_path)
        print("File Path Test Output:", data)
    else:
        print(f"File not found: {script_path}")

    # Example 2: Raw text input
    raw_text = "A superhero flies over the city at sunset. The hero smiles at the crowd below."
    data = parse_script(raw_text)
    print("Raw Text Test Output:", data)