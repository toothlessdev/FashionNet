import requests
import numpy as np
import os
from PIL import Image

from sklearn.neighbors import KNeighborsClassifier

class ItemImage:
    def __init__(self, image_url, neighbors=5):
        self.image = Image.open(requests.get(url=image_url, stream=True).raw)

    
    # image_pixel 에 모든 pixel 에 대해 KNN 알고리즘으로 5개로 군집화
    def get_colors(self):
        pass


    # 
    def get_principle_color(self):
        pass



if __name__ == "__main__":

    with open("testImage1.jpeg", "rb") as f:
        image = Image.open(f)
        image_pixel = np.asarray(image)
        image_width, image_height = image.size

        print(image_width, image_height)
        print(image_pixel.shape)