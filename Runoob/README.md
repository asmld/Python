# Runoob
The questions in `Runoob` and answers to them.

[Click here to view the questions on its original page](https://www.runoob.com/python/python-100-examples.html)

+ [Question 1 to 5](#question-1)
+ [Question 6 to 10](#question-6)

[![`Loop`](https://img.shields.io/badge/-Loop-brightgreen)](https://www.runoob.com/python3/python3-loop.html)
[![`Condition`](https://img.shields.io/badge/-Condition-yellow)](https://www.runoob.com/python3/python3-conditional-statements.html)
[![`String`](https://img.shields.io/badge/-String-red)](https://www.runoob.com/python3/python3-string.html)
[![`Math`](https://img.shields.io/badge/-Math-blue)](123)
[![`List`](https://img.shields.io/badge/-List-orange)](https://www.runoob.com/python3/python3-list.html)
[![`Function`](https://img.shields.io/badge/-Function-lightgrey)](https://www.runoob.com/python/python-functions.html)

------

### Question 1:

[![`Loop`](https://img.shields.io/badge/-Loop-brightgreen)](https://www.runoob.com/python3/python3-loop.html)
[![`Condition`](https://img.shields.io/badge/-Condition-yellow)](https://www.runoob.com/python3/python3-conditional-statements.html)

**题目描述**：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

> **提示**：通过三层嵌套循环来实现

**输出样例**：

```
共有 24 个数满足条件
它们分别是： [123, 124, 132, 134, 142, 143, 213, 214, 231, 234, 241, 243, 312, 314, 321, 324, 341, 342, 412, 413, 421, 423, 431, 432]
```

**源码**：[Question1.py](https://github.com/asmld/Python/blob/master/Runoob/Question1.py)

**分析**：无

### Question 2:

[![`Condition`](https://img.shields.io/badge/-Condition-yellow)](https://www.runoob.com/python3/python3-conditional-statements.html)
[![`String`](https://img.shields.io/badge/-String-red)](https://www.runoob.com/python3/python3-string.html)

**题目描述**：企业发放的奖金根据利润提成。利润低于或等于10万元时，奖金可提成10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分可提成7.5%；利润20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时，高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成。输入当月利润（万元），输出应发放奖金总数（万元，保留两位小数）。

> **提示**：可通过 `if-elif-else` 语句实现

**输出样例**：

```
请输入当月利润（万元）：33
应发奖金2.40万元
```

**源码**：[Question2.py](https://github.com/asmld/Python/blob/master/Runoob/Question2.py)

**分析**：无

### Question 3:

[![`Math`](https://img.shields.io/badge/-Math-blue)](123)

**题目描述**：求所有不小于-100的整数，满足加上100后是一个完全平方数，再加上168又是一个完全平方数。

> 提示：通过数学推导确定数的范围

**输出样例**：

```
[-99, 21, 261, 1581]
```

**源码**：[Question3.py](https://github.com/asmld/Python/blob/master/Runoob/Question3.py)

**分析**：

1. 确定范围：

   ![latex](https://latex.codecogs.com/svg.image?\inline&space;n&plus;100=a^2,n&plus;268=b^2\Rightarrow&space;b^2-a^2=168&space;)

   ![latex](https://latex.codecogs.com/svg.image?\inline&space;b>a\Rightarrow&space;b\geq&space;a&plus;1)

   ![latex](https://latex.codecogs.com/svg.image?\inline&space;168=b^2-a^2\geq(a&plus;1)^2-a^2=2a&plus;1)

   ![latex](https://latex.codecogs.com/svg.image?\inline&space;a<84)

2. 只需通过循环求出所有满足![latex](https://latex.codecogs.com/svg.image?\inline&space;\sqrt{a^2&plus;168}\in&space;\mathbb{Z})的 `a`
3. ![latex](https://latex.codecogs.com/svg.image?\inline&space;a^2-100) 即为要求的 `n`

### Question 4:

[![`Condition`](https://img.shields.io/badge/-Condition-yellow)](https://www.runoob.com/python3/python3-conditional-statements.html)
[![`Math`](https://img.shields.io/badge/-Math-blue)](123)
[![`String`](https://img.shields.io/badge/-String-red)](https://www.runoob.com/python3/python3-string.html)

**题目描述**：输入某年某月某日，输出这一天是这一年的第几天。（输入格式：Y-M-D，如2021-4-18）

> **提示**：分为平年和闰年两种情况

**输出样例**：

```
请输入日期（如2021-4-18）：2021-1-23
2021-1-23是2021年的第23天
```

**源码**：[Question4.py](https://github.com/asmld/Python/blob/master/Runoob/Question4.py)

**分析**：

1. 通过 [`split`](https://www.runoob.com/python/att-string-split.html) 方法从输入的字符串中获取到年、月、日
2. 判断是闰年还是平年
3. 根据月、日分析计算出天数
4. 利用[正则表达式](https://www.runoob.com/python/python-reg-expressions.html )判断输入的格式是否正确并进行[异常处理](https://www.runoob.com/python/python-exceptions.html )（进阶）

### Question 5:

[![`Loop`](https://img.shields.io/badge/-Loop-brightgreen)](https://www.runoob.com/python3/python3-loop.html)
[![`List`](https://img.shields.io/badge/-List-orange)](https://www.runoob.com/python3/python3-list.html)

**题目描述**：先输入一个正整数 `n`，然后输入 `n` 个整数，从大到小输出这些数。

> **提示**：把输入的数放进列表中，再使用 [`sort`](https://www.runoob.com/python3/python3-att-list-sort.html) 方法

**输出样例**：

```
4
请输入第1个数：6
请输入第2个数：8
请输入第3个数：3
请输入第4个数：4
8 6 4 3 
```

**源码**：[Question5.py](https://github.com/asmld/Python/blob/master/Runoob/Question5.py)

**分析**：无

### Question 6：

[![`Loop`](https://img.shields.io/badge/-Loop-brightgreen)](https://www.runoob.com/python3/python3-loop.html)
[![`Function`](https://img.shields.io/badge/-Function-lightgrey)](https://www.runoob.com/python/python-functions.html)

**题目描述**：输入 `n` ，输出[斐波拉契数列](https://baike.baidu.com/item/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/99145)的第 `n` 项

> **提示**：通过循环或者函数的递归实现

**输出样例**：

```
请输入项数：10
55
```

**源码**：[Question6.py](https://github.com/asmld/Python/blob/master/Runoob/Question6.py)

**分析**：无