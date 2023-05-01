from style import *
from bs4 import BeautifulSoup

import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()

style_lists = get_style_lists(page_index=1)

for style_list in style_lists[0:2]:
    print(f"codimap/views/{style_list}")
    style_info = get_style_info(style_list)

    # 새로운 /codimap/views 의 시작 node index
    style_group = list()
    
    for item in style_info:
        item_info = get_item_info(item)
        print(f"/goods/{item} ", end="")
        print(f"{item_info}")

        # /goods/{item} 마다 노드번호 item 부여
        # 해당 노드에 category attribute 추가
        style_group.append(item)
        G.add_node(node_for_adding=item, attr={"category" : item_info["category"]})

    # /codimap/views 에 있는 items (style_group)끼리 edges로 연결
    for idx in range(len(style_group)-1):
        G.add_edge(style_group[idx], style_group[idx+1], weight=10)


# 서로 다른 카테고리(대분류)에 속해있지만
# 코디로 묶이지 않아 간선이 없는 노드에 대해
# 간선을 추가하고 음의 가중치를 부여한다.
for src in list(G.nodes()):
    for dst in list(G.nodes()):
        if src != dst:
            src_category = G.nodes[src]["attr"]["category"]
            dst_category = G.nodes[dst]["attr"]["category"]
            if not G.has_edge(src, dst):
                if src_category != dst_category:
                    G.add_edge(src, dst, weight=-50)
                else:
                    G.add_edge(src, dst, weight=10)




# draw graph with weighted edges
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)
nx.draw_networkx_edge_labels(G,pos)
plt.show()



