import os
import torch
from diffusers import StableDiffusionPipeline

# Initialize the pipeline once
def initialize_pipeline():
    model_path = "runwayml/stable-diffusion-v1-5"  # Path to your Stable Diffusion model
    pipeline = StableDiffusionPipeline.from_pretrained(
        model_path, torch_dtype=torch.float16
    ).to("cuda")  # Move to GPU for acceleration
    print("Pipeline initialized successfully!")
    return pipeline

# Use the preloaded pipeline for image generation
def generate_image(prompt, output_path, pipeline):
    directory = os.path.dirname(output_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created missing directory: {directory}")

    print(f"Generating image with prompt: {prompt}")
    print(f"Saving image to: {output_path}")

    # Generate the image
    image = pipeline(prompt).images[0]

    try:
        image.save(output_path)
        print(f"Image successfully saved to {output_path}")
    except Exception as e:
        print(f"Error while saving the image: {e}")
        raise
    
if __name__ == "__main__":
    # Initialize the pipeline
    pipeline = initialize_pipeline()

    # Test image generation with sample prompts
    test_prompts = [
        "A superhero flying over the city at sunset",
        "A futuristic city skyline with glowing neon lights"
    ]
    for i, prompt in enumerate(test_prompts):
        output_path = f"./assets/generated_panels/test_image_{i + 1}.png"
        generate_image(prompt, output_path, pipeline)