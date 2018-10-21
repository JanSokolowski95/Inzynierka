from PIL import Image

def handle_uploaded_file(image):
    img = Image.open(image)
    img.show()
