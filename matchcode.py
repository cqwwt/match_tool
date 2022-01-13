import pandas as pd
from fuzzywuzzy import fuzz
import heapq


def max_Three_num_index(array):
    re1 = map(array.index, heapq.nlargest(3, array))  # 求最大的三个索引    nsmallest与nlargest相反，求最小
    return list(re1)  # 因为re1由map()生成的不是list，直接print不出来，添加list()就行了


def max_Three_num_percent(array):
    re2 = heapq.nlargest(3, array)  # 求最大的三个元素
    return re2


def match_operation(filename_data, filename_library, column_data, column_library, save_finalData, save_matchData):
    df_prev = pd.read_excel(filename_data)

    df_data = pd.read_excel(filename_data, usecols=[column_data])  # 读取列
    df_library = pd.read_excel(filename_library, usecols=[column_library])

    new_name = ['型号']
    df_data.columns = new_name
    df_library.columns = new_name
    a = df_data["型号"].values
    b = df_library["型号"].values
    max_index = []
    max_percent = []

    for i in range(len(a)):
        top_three_array = []
        for j in range(len(b)):
            accuracy = fuzz.ratio(a[i], b[j])
            top_three_array.append(accuracy)

        max_index.append(max_Three_num_index(top_three_array))
        max_percent.append(max_Three_num_percent(top_three_array))

    max_value = []
    for i in range(len(max_index)):
        max_value.append(b[max_index[i]])

    df_max_value = pd.DataFrame(max_value)
    df_max_percent = pd.DataFrame(max_percent)
    df_all = pd.DataFrame(a)
    col = ['原始数据']
    df_all.columns = col

    df_all.insert(1, '匹配数据1', df_max_value[0])
    df_all.insert(2, '准确率1', df_max_percent[0])
    df_all.insert(3, '匹配数据2', df_max_value[1])
    df_all.insert(4, '准确率2', df_max_percent[1])
    df_all.insert(5, '匹配数据3', df_max_value[2])
    df_all.insert(6, '准确率3', df_max_percent[2])
    df_all.insert(7, '修改后数据', '')

    for i in range(len(df_all)):
        if df_all['准确率1'][i] == 100:
            df_all.loc[[i], ["修改后数据"]] = df_all.loc[[i], ["匹配数据1"]].values

    df_final = pd.concat([df_prev, df_all["修改后数据"]], axis=1)

    df_final.to_excel(save_finalData + '/原数据+修改列.xlsx', sheet_name='sheet_1')
    df_all.to_excel(save_matchData + "/匹配表.xlsx", sheet_name='sheet_1')




# filename_data = "/Users/gregorycui/Desktop/数据.xlsx"
# filename_library = "/Users/gregorycui/Desktop/库.xlsx"
#column_data = 2
#column_library = 0
# save_finalData = '/Users/gregorycui/Desktop/原数据+修改列.xlsx'
# save_matchData = '/Users/gregorycui/Desktop/匹配表.xlsx'
# match_operation(filename_data, filename_library, column_data, column_library, save_finalData, save_matchData)