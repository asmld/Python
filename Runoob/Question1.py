n = 0
num = []
for i in range(1, 5):  # 回顾range函数的返回范围
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and k != i:  # 思考：此条件有没有更简单的写法？
                n = n + 1
                num.append(100 * i + 10 * j + k)
print('共有', n, '个数满足条件')
print('它们分别是：', num)  # 思考：如何去除输出结果中的“[”和“]”?
