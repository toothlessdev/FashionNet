from style import *
from bs4 import BeautifulSoup

style_lists = get_style_lists(page_index=1)

for style_list in style_lists[0:10]:
    print(f"codimap/views/{style_list}")
    style_info = get_style_info(style_list)
    for item in style_info:
        print(get_item_info(item))
    print()

print(style_lists)
print(len(style_lists))