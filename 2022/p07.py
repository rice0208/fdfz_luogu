r"""
(c) 2023 by rice0208, licensed under MIT.

# 解方程

## 题目描述

给定三个整数 $a$，$b$，$c$，请解方程 $ax^2+bx+c=0$。  
        
注意：这里的系数$a$可以等于$0$

## 输入格式

三行，每行一个整数，分别表示 $a$，$b$，$c$

## 输出格式

如果方程无解，请输出 No Answer ；    
如果方程有一个或两个解，请按照从小到大输出解；      
如果方程有无穷多解，请输出 infinite solutions
      
所有的解保留1位小数

## 样例 #1

### 样例输入 #1

```
1
-5
6
```

### 样例输出 #1

```
2.0
3.0
```

## 样例 #2

### 样例输入 #2

```
1
1
1
```

### 样例输出 #2

```
No Answer
```

## 样例 #3

### 样例输入 #3

```
0
0
1
```

### 样例输出 #3

```
No Answer
```

## 样例 #4

### 样例输入 #4

```
0
0
0
```

### 样例输出 #4

```
infinite solutions
```

## 样例 #5

### 样例输入 #5

```
0
2
1
```

### 样例输出 #5

```
-0.5
```

## 样例 #6

### 样例输入 #6

```
0
3
-1
```

### 样例输出 #6

```
0.3
```

## 样例 #7

### 样例输入 #7

```
1
-4
4
```

### 样例输出 #7

```
2.0
2.0
```
"""

from math import sqrt

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("infinite solutions")
        else:
            print("No Answer")
    else:
        print(round(-c / b, 1))
else:
    dt = b * b - 4 * a * c
    if dt < 0:
        print("No Answer")
    else:
        r = sqrt(dt)
        if a > 0:
            print(round((-b - r) / (2 * a), 1))
            print(round((-b + r) / (2 * a), 1))
        if a < 0:
            print(round((-b + r) / (2 * a), 1))
            print(round((-b - r) / (2 * a), 1))
