n = int(input())  # 回顾：input函数返回的永远是字符串
num = []
for i in range(n):
    num.append(int(input('请输入第%d个数：' % (i + 1))))  # 思考：此循环如何实现把输入的n个数放进列表的？
num.sort(reverse=True)  # 思考：如果使用sorted函数该如何写？
for i in num:
    print(i, end=' ')  # 回顾：print函数的几个参数
