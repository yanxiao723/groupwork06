import re
def data_getting(files):
    with open(files) as f: # get row data
        cont = f.read()
    comp = re.compile('[0-9]' '[0-9]' '[0-9]' '[0-9]' '[0-9]') # remove the five-digit serial number
    data_useless = comp.findall(cont)
    uselessdata = []
    for i in data_useless:
        uselessdata.append(i)
    Datarow = cont.split()
    Data = Datarow[4: ]
    data = []
    for i in Data:
        if i in uselessdata:
            pass
        else:
            data.append(int(i))
    return data

def list_of_groups(init_list, children_list_len): # to get the list into parts with given length.
    list_of_groups = zip(*(iter(init_list),) *children_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list

def final_data(files, children_list_len): # the final data is the list of a month that contains the data of each days.
    data = data_getting(files)
    final_list = list_of_groups(data, children_list_len)
    return final_list
