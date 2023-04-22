from style import *

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = 'NanumSquare.ttf'
fontprop = fm.FontProperties(fname=font_path)



if __name__ == "__main__":
    plt.rcParams['font.family'] = 'NanumSquare'
    plt.rcParams['font.size'] = 8

    graph = nx.Graph()

    node_index_start = 1

    node_index = node_index_start
    style_info = get_style_info(22589)

    # add Nodes
    for item in style_info:
        node_attr = get_item_info(item)
        graph.add_node(node_for_adding=node_index, label=str(node_attr))
        node_index += 1

    # add Edges
    for index in range(node_index):
        graph.add_edge(index, index+1)

    node_index_start = node_index


    nx.draw(graph, with_labels=True)
    labels = nx.get_node_attributes(graph, 'label')
    nx.draw_networkx_labels(graph, pos=nx.spring_layout(graph), labels=labels, font_family='NanumSquare', font_size=12)
    plt.show()

