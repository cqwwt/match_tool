import pandas as pd


def clean_code(filename_address, column, save_address):
    df = pd.read_excel(filename_address)
    df_clean = pd.read_excel(filename_address, usecols=[column])  # 读取列

    new_name = ['清理后']
    df_clean.columns = new_name

    # 数据清理逻辑
    df_clean.replace('\s+', '', regex=True, inplace=True)
    df_clean.replace('a', 'A', regex=True, inplace=True)

    # 把清理后的数据插入原表最后一列并保存
    df.insert(column + 1, "清理后", df_clean['清理后'])
    # df = pd.concat([df, df_clean], axis=1)
    df.to_excel(save_address, sheet_name='sheet1')


filename_address = '/Users/gregorycui/Desktop/clean.xlsx'
column = 0
save_address = "/Users/gregorycui/Desktop/clean_.xlsx"
clean_code(filename_address, column, save_address)
