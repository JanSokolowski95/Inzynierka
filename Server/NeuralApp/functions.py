from PIL import Image
import numpy as np
from .predict import Network
from django.conf import settings

def handle_uploaded_file(image):
    img = Image.open(image)
    img = img.resize((224, 224), Image.ANTIALIAS)
    
    network = Network(settings.WEIGHTS_PATH)

    result = network.predict(img)
    
    #img.show()
    return result
