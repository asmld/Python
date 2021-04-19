import pandas as pd
data1 = pd.read_excel('./NCV.xls', sheet_name='Sheet1')
df = pd.DataFrame(columns=['时间', '确诊', '日增', '死亡', '国家'])
col = ['时间', '确诊', '日增', '死亡', '国家']
for i in range(25):
    data = data1.iloc[1:,[0, 3*i+1, 3*i+2, 3*i+3]]
    country = data.columns[1]
    data['国家'] = country
    dic = {data.columns[x]: col[x] for x in range(5)}
    data = data.rename(columns=dic)
    df = pd.concat([df, data], ignore_index=True, axis=0)
df.to_excel('ncv_result.xlsx')
