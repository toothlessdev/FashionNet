import numpy as np

# 먼셀의 10색상환 + 무채색 3가지 (검정, 회색, 흰색)

color_categories = {
    "white":np.array([255,255,255]),
    "gray":np.array([178,178,178]),
    "black":np.array([0,0,0]),

    "red":np.array([255,0,0]),
    "orange":np.array([251,132,2]),
    "yellow":np.array([255,252,1]),
    "lightgreen":np.array([64,203,119]),
    "green":np.array([39,137,42]),
    "lightblue":np.array([22,152,189]),
    "blue":np.array([0,82,167]),
    "navy":np.array([0,42,149]),
    "purple":np.array([152,18,141]),
    "pink":np.array([222,5,106]),
}



color_categories_ = {
    '화이트': np.array([220,220,220]),
    '블랙': np.array([50,50,50]),
    '그레이': np.array([178,178,178]),
    '베이지':np.array([206,179,144]),
    '브라운':np.array([127,41,12]),

    # R 계열
    '레드':np.array([255,0,0]),
    '오렌지':np.array([249,40,1]),
    '옐로우':np.array([254,234,1]),
    '핑크':np.array([248,6,161]),

    # G 계열
    '그린':np.array([54,176,0]),
    '카키':np.array([91,90,53]),

    # B 계열
    '블루': np.array([39,47,255]),
    '스카이블루':np.array([35,195,235]),
    '네이비': np.array([0,32,102]),
    '민트':np.array([50,196,171]),
    
    '퍼플':np.array([87,12,112]),
}