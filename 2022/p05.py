r"""
(c) 2023 by rice0208, licensed under MIT.

# 判断三角形的类型

## 题目描述

输入三角形的三边长度(正整数)，判断这个三角形的类型，是等边(DB)，等腰(DY)，还是一般(YB)三角形。      

本题中，等边和等腰是两种$\color{Red}\textbf{不同}$的三角形。

## 输入格式

一共3行，每行一个正整数。

## 输出格式

DB 或 DY 或 YB；如果无法构成三角形，则输出 ERROR。

## 样例 #1

### 样例输入 #1

```
1
2
3
```

### 样例输出 #1

```
ERROR
```

## 样例 #2

### 样例输入 #2

```
9
9
5
```

### 样例输出 #2

```
DY
```

## 样例 #3

### 样例输入 #3

```
9
9
9
```

### 样例输出 #3

```
DB
```

## 样例 #4

### 样例输入 #4

```
3
4
5
```

### 样例输出 #4

```
YB
```
"""

a = int(input())
b = int(input())
c = int(input())

if a >= b + c or b >= c + a or c >= a + b:
    print("ERROR")
elif a == b:
    if a == c:
        print("DB")
    else:
        print("DY")
elif a == c or b == c:
    print("DY")
else:
    print("YB")
