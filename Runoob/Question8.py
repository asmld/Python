for i in range(1, 10):
    for j in range(i, 10):
        r = str(i * j)
        blank = ' ' if len(r) == 1 else ''  # 此变量用于对齐，不要求掌握
        print(str(i)+'X'+str(j)+'='+r+blank, end=' ')  # 回顾：字符串的加法运算
    print()  # 思考：此句作用？
