from PIL import Image
import numpy as np
from .predict import Network

def handle_uploaded_file(image):
    img = Image.open(image)
    img = img.resize((224, 224), Image.ANTIALIAS)
    
    network = Network('./NeuralApp/weights.h5')

    result = network.predict(img)
    
    #img.show()
    return result
