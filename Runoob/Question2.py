a = float(input('请输入当月利润（万元）：'))  # 思考：为什么此处用float而非int？
b = 0  # 思考：此句能否删去？
if 0 <= a <= 10:
    b = 0.1 * a
elif a <= 20:
    b = 1 + (a - 10) * 0.075
elif a <= 40:
    b = 1.75 + (a - 20) * 0.05
elif a <= 60:
    b = 2.75 + (a - 40) * 0.03
elif a <= 100:
    b = 3.35 + (a - 60) * 0.015
else:
    b = 3.95 + (a - 100) * 0.01
print('应发奖金%.2f万元' % b)  # 记住这个用法，思考：如果用format函数该如何写？（建议掌握，见https://www.runoob.com/python/att-string-format.html）
