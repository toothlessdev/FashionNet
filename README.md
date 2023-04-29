<h1 style="font-size:40px; text-align:center;">FashionNet</h1>

<h2>사용한 패키지, 라이브러리</h2>
1. Beautiful Soup (pyton) - Web Crawling<br>
2. Scikit Learn (python) - Image Pixel KMeans (의류 색상 추출)<br>
3. NetworkX, Matplotlib (python) - Network 시각화 <br>
4. Express (node.js) - REST API <br>
3. neo4j (DB) - Graph DB Library<br>

<br>

<h2>데이터 저장</h2>
1. 의류 쇼핑몰에서 코디 정보들을 크롤링<br>
2. 착장 이미지에 대해 Meta 의 SAM 모델을 통해 의류를 분리후 저장<br>
3. 추후 서비스 사용자들이 많아지면, 코디를 등록하고 서로 평가를 통해 좋은 평가를 받는 코디를 저장

<br>

<h2>네트워크 분석</h2>
1. 동일 카테고리(대분류)끼리는 간선을 연결하지 않음<br>
2. 코디로 묶여있는 의류끼리는 간선을 연결하고, 가중치를 높게 부여<br>
3. 서로 다른 카테고리(대분류)에 속해있지만, 코디로 묶이지 않아 간선이 없는 노드끼리는<br>
간선을 추가하고 음의 가중치를 부여한다<br>
<br>

<h2>적용</h2>
1. 네트워크의 매개 중심성(Betweenness Centrality) 분석을 진행<br>
2. 사용자가 이미 가지고 있는 의류에 특정한 의류를 추가하면 많은 코디를 완성시킬 수 있다면<br>
3. 해당 의류를 추천해주는 시스템<br>

<br><br><br><br><br><br><br><br>

<h2>Tasks</h2>
<h4>● get_style_list 함수구현 : /codimap/lists?page 로 부터 /codimap/views/ 에 들어갈 index 파싱 (23.4.23)</h4>
<h4></h4>
<h4>○ Item 클래스 만들어서 image.py 에 ItemImage 클래스 상속</h4>
<h4>○ style.py 에 get_item_info 에서 Item 클래스 리턴하도록 수정</h4>
<h4>● </h4>

<br><br><br><br>

<h1><strong>style.py</strong></h1>

<h2><strong>Functions</strong></h2>

```python
def get_style_info(index)
```

<h3><li><strong> PARAMETERS : </strong></li></h3>

index(int) : 무신사 코디맵 URL https://www.musinsa.com/app/codimap/views/ 뒤에 오는 정수 파라미터

<h3><li><strong> RETURNS : </strong></li></h3>

item_array(list) : 해당 코디를 구성하고있는 의류에 대한 URL parameter list 리턴

<h3><li><strong> RAISES : </strong></li></h3>

<br>

```python
def get_item_info(index)
```

<h3><li><strong> PARAMETERS : </strong></li></h3>

index (int) : 무신사 item URL https://www.musinsa.com/app/goods/ 뒤에 오는 정수 파라미터

<h3><li><strong> RETURNS : </strong></li></h3>

item_info (dict) : 해당 item 에 대한 카테고리, 주요색상 등의 정보를 담은 dictionary 리턴

<h3><li><strong> RAISES : </strong></li></h3>

HttpForbiddenException : request 404 error

<br><br>

# <strong>image.py</strong>

<h2><strong>Class</strong></h2>

```python
class ItemImage:
    def __init__(self, image_url, resize_size=(100,100), url_web=True)
    def get_principle_color(self, n=4, limit=0.05)
    def get_principle_color_kmeans(self, n=4)
```

<br><br>

<h2><strong>Methods</strong></h2>

```python
def __init__(self, image_url, resize_size=(100,100), url_web=True)
```

<h3><li><strong> PARAMETERS : </strong></li></h3>

image_url (str) : 이미지에 대한 url <br>
resize (bool) : 성능 향상을 위해 이미지 사이즈 축소 여부<br>
resize_size (tuple) : resize 가 True 일때 축소된 이미지 size (width, height)<br>
url_web (bool) : image_url 이 web url 일때 True 사용<br>

<br><br>

```python
def get_principle_color_kmeans(self, cluster_size=4, symbol_output=False)
```

<h3><li><strong> PARAMETERS : </strong></li></h3>

cluster_size (int) : kmeans 사용시 군집의 개수

symbol_output (boolean) : return type 을 symbol로 설정

<h3><li><strong> RETURNS : </strong></li></h3>

colors (list) : kmeans 로 군집화된 cluster_size 의 [r, g, b] 쌍의 list

<br><br>
