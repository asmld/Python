# 函数递归法
def f(x):
    if x == 1 or x == 2:
        return 1
    else:
        return f(x - 1) + f(x - 2)


n = int(input('请输入项数：'))
print(f(n))

# 循环法
n = int(input('请输入项数：'))
b = c = 1  # 注意：这也是合法定义
for i in range(n - 2):  # 思考：为什么是n-2？
    b, c = c, b + c  # 思考：如何实现了多次相加？
print(c)
