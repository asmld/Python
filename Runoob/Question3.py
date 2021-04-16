nums = []
for a in range(84):
    b = (a ** 2 + 168) ** 0.5
    if b == int(b):  # 思考：此条件为什么这么写？
        nums.append(a ** 2 - 100)
print(nums)
