import requests
from bs4 import BeautifulSoup

import numpy
from PIL import Image

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

class HttpForbiddenException(Exception):
    def __init__(self, status_code, url):
        super().__init__(f"HTTP Forbidden Exception : {status_code} on {url})")


def get_style_info(index):
    item_array = list()
    url = "https://www.musinsa.com/app/codimap/views/"
    response = requests.get(url=url + str(index), headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("a", "brand_item")

        for item in items:
            item_array.append(item["href"].lstrip("/app/goods/").rstrip("/0"))
        return item_array
        
    else:
        raise HttpForbiddenException(response.status_code, url+str(index))

def get_item_info(index):
    url = "https://musinsa.com/app/goods/"
    response = requests.get(url=url + str(index), headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        category = soup.select("div.product_info > p > a")[0].text
        category_sub = soup.select("div.product_info > p > a")[1].text

        item_info = {
            "category" : category,
            "category_sub" : category_sub,
        }
        return item_info

    else:
        raise HttpForbiddenException(response.status_code, url+str(index))

def get_principle_color(image_url):
    image = Image.open(requests.get(url=image_url, stream=True).raw)
    image_pixel = numpy.asarray(image)

    

    image.close()

