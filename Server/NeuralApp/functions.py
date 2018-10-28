from PIL import Image
import numpy as np
#from .predict import Network

def handle_uploaded_file(image):
    img = Image.open(image)
    img = img.resize((224, 224), Image.ANTIALIAS)

    #result = Network.predict(img)
    
    #img.show()
    return ['it', 'just', ' works']
