import re


date = input('请输入日期（如2021-4-18）：')
pattern = r'^\d{1,4}-\d{1,2}-\d{1,2}$'
result = re.match(pattern, date)
if not result:
    raise ValueError('Invalid date form "%s"' % date)
date_list = date.split('-')
year = int(date_list[0])  # 注意：将字符串转换为整型
month = int(date_list[1])
day = int(date_list[2])
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # 回顾：闰年的判断条件
    day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if month > 12 or day > day_list[month - 1]:
    raise ValueError('Invalid date form "%s"' % date)
n = 0
for i in range(month - 1):
    n = n + day_list[i]
n = n + day
print('%s是%d年的第%d天' % (date, year, n))  # 思考：如何将输出效果改为“Y年M月D日是Y年的第n天”？
