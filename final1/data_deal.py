"""
@author:Delin Fan
ID:320180939721
"""


import matplotlib.pyplot as plt

def data_predealing(clean_list: list):
    x = [i for i in range(24)]#j建立列表
    plt.plot(x, clean_list)#绘制出新数据的图
    plt.show()