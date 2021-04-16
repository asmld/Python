import pandas as pd


def f(j):
    s = col[j]
    s = s[3:]
    s = s.strip('()')
    return s


data = pd.read_excel('./industry.xls')  # 此处为表格的路径
print(data)
col = data.columns
print(col)
myList = []
for i in range(137):
    for j in range(2, 45):
        if data.iloc[i, j]:
            myList.append(f(j))
print(myList)
