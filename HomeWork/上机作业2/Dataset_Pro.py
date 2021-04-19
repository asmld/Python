import pandas as pd
f = pd.ExcelFile('./Dataset_city.xlsx')
data = pd.DataFrame(columns=['时间段', '标题', '摘要', '网址'])
for i in f.sheet_names:
    data1 = pd.read_excel('./Dataset_city.xlsx', sheet_name=i)
    data1 = data1.iloc[:, [13, 14, 15]]
    data1['时间段'] = i
    data1.reindex(columns=['时间段', '标题', '摘要', '网址'])
    data = pd.concat([data, data1], axis=0, ignore_index=True)
data.to_excel('result_1.xlsx')
