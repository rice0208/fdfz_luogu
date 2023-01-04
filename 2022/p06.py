r"""
(c) 2023 by rice0208, licensed under MIT.

# 某年某月的天数

## 题目描述

如果告诉你年份和月份，你能告诉我这一年的这个月有多少天吗？

## 输入格式

输入数据包括2行，每行1个正整数，分别表示年份和月份。

## 输出格式

输出1个整数。表示该月的天数。

## 样例 #1

### 样例输入 #1

```
2019
4
```

### 样例输出 #1

```
30
```

## 样例 #2

### 样例输入 #2

```
2019
2
```

### 样例输出 #2

```
28
```

## 样例 #3

### 样例输入 #3

```
2000
2
```

### 样例输出 #3

```
29
```

## 样例 #4

### 样例输入 #4

```
1900
2
```

### 样例输出 #4

```
28
```

## 提示

判断闰年的方法是：年份能被400整除，或者年份能被4整除但是不能被100整除。
"""

y = int(input())
m = int(input())

if m == 2:
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                d = 29
            else:
                d = 28
        else:
            d = 29
    else:
        d = 28
elif m <= 7:
    if m % 2 == 0:
        d = 30
    else:
        d = 31
else:
    if m % 2 == 0:
        d = 31
    else:
        d = 30

print(d)
