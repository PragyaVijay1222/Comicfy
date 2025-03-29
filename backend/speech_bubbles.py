from PIL import Image, ImageDraw, ImageFont

def add_speech_bubble(image_path, text, bubble_position, font_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Draw speech bubble
    bubble_width, bubble_height = 200, 100
    bubble_x, bubble_y = bubble_position
    draw.rectangle([bubble_x, bubble_y, bubble_x + bubble_width, bubble_y + bubble_height], fill="white", outline="black")
    
    # Add text to speech bubble
    font = ImageFont.truetype(font_path, size=20)
    text_position = (bubble_x + 10, bubble_y + 10)
    draw.text(text_position, text, fill="black", font=font)

    image.save(image_path)
    print(f"Updated image saved to {image_path}")

if __name__ == "__main__":
    add_speech_bubble("./assets/generated_panels/superhero.png", "I'm here to save the day!", (50, 50), "./assets/fonts/arial.ttf")