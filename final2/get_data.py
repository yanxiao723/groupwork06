def get_log(files):
    with open(files) as f:
        data_log = f.read()
        data_list = data_log.split()
        data_count={}
        for datas in data_list:
            data_count[datas]=data_count.get(datas,0)+1
    return data_count