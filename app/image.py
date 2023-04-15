import requests
import numpy as np
import os
from PIL import Image
import colortable
import math

def get_square_distance(color1, color2):
    return np.sum(np.square(color1-color2))

# color_categories 와 color를 비교해서 euclidian distance 가 가까운 색상의 key값 리턴
def get_color_symbol(color):
    color_symbol = ""
    color_distance = math.inf

    for key, item in colortable.color_categories.items():
        distance = get_square_distance(item, color)
        if color_distance > distance:
            color_distance = distance
            color_symbol = str(key)
    return color_symbol
    

class ItemImage:
    def __init__(self, image_url, resize_size=(100,100), url_web=True):
        if url_web:
            self.image = Image.open(requests.get(url=image_url, stream=True).raw).resize(resize_size)
        else:
            self.image = Image.open(image_url).resize(resize_size)

        self.image_pixel = self.image.convert('RGB')

        self.colors = dict()
        self.principle_color = dict()

        for key, item in colortable.color_categories.items():
            self.colors[key] = 0

    def get_resized_image(self):
        self.image.save("resized.jpg")

    def get_colors(self):
        for row in range(self.image_pixel.width):
            for col in range(self.image_pixel.height):
                color = np.array(self.image_pixel.getpixel((row,col)))
                self.colors[get_color_symbol(color=color)] += 1
        self.colors = sorted(self.colors.items(), key = lambda item: item[1], reverse=True)

        return self.colors

    # 주 색상 n개 리턴, limit 비율 보다 적은 색상은 버림 (기본값 0.05)
    def get_principle_color(self, n=4, limit=0.05):
        for key, value in self.colors:
            if value > self.image.width * self.image.height * limit:
                self.principle_color[key] = value
        return self.principle_color



if __name__ == "__main__":
    # test code for image.py
    # img = ItemImage("https://image.msscdn.net/images/goods_img/20230210/3074892/3074892_16760091686503_500.jpg", url_web=True)
    img = ItemImage("https://image.msscdn.net/images/goods_img/20210808/2052494/2052494_1_500.jpg")
    colors= img.get_colors()

    for color in colors:
        print(color)

    principle_colors = img.get_principle_color()
    for c in principle_colors:
        print(c)

    img.get_resized_image()