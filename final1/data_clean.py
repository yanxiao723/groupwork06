import numpy as np

# the type of row_list should be the list of lists.
def data_cleaning(row_list: list):
    midd_list = []
    hours = len(row_list[0])
    for i in range(hours):
        mid_list = []
        for j in range(len(row_list)):
            mid_list.append(row_list[j][i])
        midd_list.append(mid_list)
    mean_value = []
    for i in midd_list:
        while np.var(i) > 100:
            i.remove(max(i))
            i.remove(min(i))
        else:
            mean_value.append(np.mean(i))
    return mean_value
