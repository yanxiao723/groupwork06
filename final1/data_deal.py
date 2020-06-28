import matplotlib.pyplot as plt

def data_predealing(clean_list: list):
    x = [i for i in range(24)]
    plt.plot(x, clean_list)
    plt.show()