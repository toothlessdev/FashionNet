import requests
from bs4 import BeautifulSoup

from image import ItemImage

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

# /app/codimap/lists?page 에서 코디정보를 담고있는 /views의 index 리턴
def get_style_lists(page_index=1):
    try:
        url="https://www.musinsa.com/app/codimap/lists?&display_cnt=60&list_kind=big&sort=date&page="
        response = requests.get(url=url + str(page_index), headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")
        style_index_lists = list()
        elements = soup.select("li.style-list-item > div.style-list-item__thumbnail > a")

        for element in elements:
            style_url = element["onclick"]
            style_url = style_url.lstrip("goView(')")
            style_url = style_url.rstrip("');")
            style_index_lists.append(int(style_url))

        return style_index_lists;


    except requests.exceptions.RequestException as e:
        print(f"http request error /app/codimap/lists : {e}")


# /app/codimap/views 에서 해당 코디를 구성하고 있는 상품의 url 을 item_array 로 리턴
def get_style_info(index):
    try:
        item_array = list()
        url = "https://www.musinsa.com/app/codimap/views/"
        response = requests.get(url=url + str(index), headers=headers)
        
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("a", "brand_item")

        for item in items:
            item_array.append(item["href"].lstrip("/app/goods/").rstrip("/0"))
        return item_array
        
    except requests.exceptions.RequestException as e:
        print(f"http request error /app/codimap/views : {e}")


def get_item_info(index):
    try:
        url = "https://musinsa.com/app/goods/"
        response = requests.get(url=url + str(index), headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        category = soup.select("div.product_info > p > a")[0].text
        category_sub = soup.select("div.product_info > p > a")[1].text
        image_url = soup.select_one("div.product-img > img")["src"]

        item_image = ItemImage("https:" + image_url)
        principle_colors = item_image.get_principle_color_kmeans(symbol_output=True)

        item_info = {
            "category" : category,
            "category_sub" : category_sub,
            "colors" : list(principle_colors)
        }
        return item_info

    except requests.exceptions.RequestException as e:
        print(f"http request error /app/goods : {e}")

