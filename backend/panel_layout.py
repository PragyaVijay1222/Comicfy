from PIL import Image

def create_comic_layout(images, output_path):
    panel_width = 800
    panel_height = 600
    layout = Image.new("RGB", (panel_width, panel_height * len(images)), "white")

    y_offset = 0
    for img_path in images:
        img = Image.open(img_path)
        img = img.resize((panel_width, panel_height))
        layout.paste(img, (0, y_offset))
        y_offset += panel_height

    layout.save(output_path)
    print(f"Comic layout saved to {output_path}")

if __name__ == "__main__":
    images = ["./assets/generated_panels/superhero.png", "./assets/generated_panels/villain.png"]
    create_comic_layout(images, "./assets/generated_panels/comic_page.png")