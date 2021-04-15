# 源码

```python
import pandas as pd


def f(j):
    s = col[j]
    s = s[3:]
    s = s.strip('()')
    return s


data = pd.read_excel('./industry.xls')
col = data.columns
myList = []
for i in range(137):
    for j in range(2, 45):
        if data.iloc[i, j]:
            myList.append(f(j))
print(myList)

```

# 详解

## 一、需求分析

> 根据 `industry.xls` 中的数据，求得**每个被试**所属的行业信息，储存在 `myList[]` 中

可以分为以下步骤：

1. 读取数据
2. 判断值是否为 `1`
3. 若为 `1` ，读取该列的列名
4. 从列名中找到行业信息
5. 储存到 `myList[]` 中

## 二、具体操作

### 1.读取表格

```python
import pandas as pd
data = pd.read_excel('./industry.xls')
myList = []
```

附：[表格预览](#1表格)

### 2.读取列名信息

```python
col = data.columns
```

附：[pandas获取列名的方法（网页）](https://blog.csdn.net/EWBA_GIS_RS_ER/article/details/90741671)、[列名预览](#2列名预览)

### 3.遍历表格，找到符合要求的数据项

```python
for i in range(137):
    for j in range(2, 45):
        if data.iloc[i, j]:
            myList.append(f(j))
```

> 1. `f(j)` 将实现返回第j列列名中相应行业的功能
> 2. `j` 从 `2` 开始遍历，是由于表格的第0列和第一列分别为 `序号` 和 `所在行业` ，第2列开始才是我们要处理的数据

附：[pandas表格索引的方法（网页）](https://blog.csdn.net/flyfish5/article/details/79852938)

### 4.从列名中获取行业名

```python
def f(j):
    s = col[j]
    s = s[3:]
    s = s.strip('()')
    return s
```

> 拿 `j=2` 举例

1. `s = col[j]`

   此时 `s` 的值为 `第7题(保险业)` ，是一个字符串

2. `s = s[3:]`

   将从 `s` 的第三个字符开始的子字符串的值赋值给 `s` ，即去除了 `第七题` ，此时 `s` 的值为 `(保险业)`

3. `s = s.strip('()')`

   去除 `s` 首尾的 `(` 或 `)` ，详见[字符串strip方法详解（网页）](https://www.runoob.com/python/att-string-strip.html)，此时 `s` 成为了我们想要的 `保险业`

4. `return s`

   返回 `s` 的值

### 5.打印 `myList`

```python
print(myList)
```



## 三、附录

### 1.表格

> 可用 `print(data)` 自行查看

```
      序号  所在行业  第7题(保险业)  第7题(采矿,能源)  ...  第7题(娱乐行业)  第7题(农业)  第7题(养殖业)  第7题(自由职业)
0      1   NaN         0           0  ...          0        0         0          0
1      2   NaN         1           0  ...          0        0         0          0
2      3   NaN         0           0  ...          0        0         0          0
3      4   NaN         0           0  ...          0        0         0          0
4      5   NaN         0           0  ...          0        0         0          0
..   ...   ...       ...         ...  ...        ...      ...       ...        ...
132  133   NaN         0           0  ...          0        0         0          1
133  134   NaN         0           0  ...          0        0         0          0
134  135   NaN         0           0  ...          0        0         0          0
135  136   NaN         0           0  ...          0        0         0          0
136  137   NaN         0           0  ...          0        0         0          0

[137 rows x 45 columns]
```

（[返回](#1读取表格)）

### 2.列名预览

> 可通过 `print(col)` 自行查看

```
['序号', '所在行业', '第7题(保险业)', ..., '第7题(养殖业)', '第7题(自由职业)']
```

（[返回](#2读取列名信息)）