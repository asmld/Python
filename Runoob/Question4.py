def check(s):
    s_list = s.split('-')
    if len(s_list) != 3:
        raise ValueError('Invalid date form "%s"' % s)
    if not (float(s_list[0]) != int(s_list[0]) and float(s_list[1]) != int(s_list[1]) and float(s_list[2]) != int(s_list[2])):
        raise ValueError('Invalid date form "%s"' % s)
    if not (0 < year and 0 < month < 13 and 0 < day <= day_list[month - 1]):
        raise ValueError('Invalid date form "%s"' % s)


date = input('请输入日期（如2021-4-18）：')
date_list = date.split('-')
year = int(date_list[0])  # 注意：将字符串转换为整型
month = int(date_list[1])
day = int(date_list[2])
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  #  回顾：闰年的判断条件
    day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
check(date)
n = 0
for i in range(month - 1):
    n = n + day_list[i]
n = n + day
print('%s是%d年的第%d天' % (date, year, n))  # 思考：如何将输出效果改为“Y年M月D日是Y年的第n天”？
