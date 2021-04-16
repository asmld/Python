# Runoob
The questions in `Runoob` and answers to them.

[Click here to view the questions on its original page](https://www.runoob.com/python/python-100-examples.html)

+ [Question 1 to 5](#question-1) 

[![`循环`](https://img.shields.io/badge/-%E5%BE%AA%E7%8E%AF-brightgreen)](https://www.runoob.com/python3/python3-loop.html)
[![`条件`](https://img.shields.io/badge/-%E6%9D%A1%E4%BB%B6-yellow)](https://www.runoob.com/python3/python3-conditional-statements.html)
[![`字符串`](https://img.shields.io/badge/-%E5%AD%97%E7%AC%A6%E4%B8%B2-red)](https://www.runoob.com/python3/python3-string.html)
[![`数学`](https://img.shields.io/badge/-%E6%95%B0%E5%AD%A6-blue)](123)

------

### Question 1:

[![`循环`](https://img.shields.io/badge/-%E5%BE%AA%E7%8E%AF-brightgreen)](https://www.runoob.com/python3/python3-loop.html)
[![`条件`](https://img.shields.io/badge/-%E6%9D%A1%E4%BB%B6-yellow)](https://www.runoob.com/python3/python3-conditional-statements.html)

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

[![`条件`](https://img.shields.io/badge/-%E6%9D%A1%E4%BB%B6-yellow)](https://www.runoob.com/python3/python3-conditional-statements.html)
[![`字符串`](https://img.shields.io/badge/-%E5%AD%97%E7%AC%A6%E4%B8%B2-red)](https://www.runoob.com/python3/python3-string.html)

**题目描述**：企业发放的奖金根据利润提成。利润低于或等于10万元时，奖金可提成10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分可提成7.5%；利润20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时，高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成。输入当月利润（万元），输出应发放奖金总数（万元，保留两位小数）。

> 提示：可通过 `if-elif-else` 语句实现

**输出样例**：

```
请输入当月利润（万元）：33
应发奖金2.40万元
```

**源码**：[Question2.py](https://github.com/asmld/Python/blob/master/Runoob/Question2.py)

**分析**：无

### Question 3:

[![`数学`](https://img.shields.io/badge/-%E6%95%B0%E5%AD%A6-blue)](123)

**题目描述**：求所有的整数，满足加上100后是一个完全平方数，再加上168又是一个完全平方数。

> 提示：通过数学推导确定数的范围

**输出样例**：

```
[-99, 21, 261, 1581]
```

**源码**：[Question3.py](https://github.com/asmld/Python/blob/master/Runoob/Question3.py)

**分析**：

1. 确定范围：

![latex](https://latex.codecogs.com/svg.image?n&plus;100=a^2,n&plus;268=b^2\,\Rightarrow\,&space;b^2-a^2=168\\\Rightarrow&space;b>a\,\Rightarrow&space;\,b\geq&space;a&plus;1\\\Rightarrow&space;\,168=b^2-a^2\geq(a&plus;1)^2-a^2=2a&plus;1\\\Rightarrow&space;\,a<84)

2. 只需通过循环求出所有满足要求的 `a`（![latex](https://latex.codecogs.com/svg.image?\inline&space;\sqrt{a^2&plus;168}\in&space;\mathbb{Z})） 
3. ![latex](https://latex.codecogs.com/svg.image?\inline&space;a^2-100) 即为要求的 `n`

