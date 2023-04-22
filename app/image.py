import requests
import numpy as np

from PIL import Image
from PIL.Image import Resampling
from sklearn.cluster import KMeans

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
    def __init__(self, image_url, resize=True, resize_size=(100,100), url_web=True):
        if url_web:
            self.image = Image.open(requests.get(url=image_url, stream=True).raw)
        else:
            self.image = Image.open(image_url)

        if resize:
            self.image = self.image.resize(size=resize_size, resample=Resampling.NEAREST)
        self.image_pixel = np.array(self.image.convert('RGB')).reshape((-1,3))



    # 주 색상 n개 리턴, limit 비율 보다 적은 색상은 버림 (기본값 0.05)
    def get_principle_color(self, n=5, limit=0.05):
        self.colors = dict()
        self.principle_color = dict()

        for key, item in colortable.color_categories.items():
            self.colors[key] = 0

        for pixel in self.image_pixel:
            self.colors[get_color_symbol(color=pixel)] += 1
        self.colors = sorted(self.colors.items(), key = lambda item: item[1], reverse=True)

        for key, value in self.colors:
            if value > self.image.width * self.image.height * limit:
                self.principle_color[key] = value
        return self.principle_color


    # k-means clustering 으로 주요 색상 추출
    def get_principle_color_kmeans(self, cluster_size=4):
        kmeans = KMeans(n_clusters=cluster_size, n_init=10).fit(self.image_pixel)
        colors = kmeans.cluster_centers_
        return colors.astype(int)



if __name__ == "__main__":
    # test code for image.py
    # img = ItemImage("https://image.msscdn.net/images/goods_img/20230210/3074892/3074892_16760091686503_500.jpg", url_web=True)
    img = ItemImage("https://image.msscdn.net/images/goods_img/20210808/2052494/2052494_1_500.jpg")

    principle_colors = img.get_principle_color()
    for c in principle_colors:
        print(c)

    print(img.get_principle_color_kmeans())

    colors = dict()
    for key, item in colortable.color_categories.items():
        colors[key] = 0
    for color in img.get_principle_color_kmeans():
        colors[get_color_symbol(color=color)] += 1
    colors = sorted(colors.items(), key = lambda item: item[1], reverse=True)
    print(colors)