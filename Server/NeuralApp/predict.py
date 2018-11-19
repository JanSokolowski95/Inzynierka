import numpy as np
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.backend import clear_session

# dimensions of our images.
(img_width, img_height) = (224, 224)
classes = ['fabric', 'foliage', 'glass', 'leather', 'metal', 'paper', 
    'plastic', 'stone', 'water', 'wood']

class Network:
    def __init__(self, weights_path):
        self.weights_path = weights_path

        self.model = VGG16(include_top=False, weights='imagenet')

        self.top_model = Sequential()
        self.top_model.add(Flatten(input_shape=(7, 7, 512)))
        self.top_model.add(Dense(256, activation='relu'))
        self.top_model.add(Dropout(0.5))
        self.top_model.add(Dense(10, activation='softmax'))
        self.top_model.load_weights(weights_path)
    
    def predict(self, img):
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        features = self.model.predict(x)
        img_class = self.top_model.predict(features)
        
        clear_session()
        return  zip(classes, img_class[0])
