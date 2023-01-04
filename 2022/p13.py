r"""
(c) 2023 by rice0208, licensed under MIT.

# 四位回文数的数量

## 题目描述

给两个正整数 $x$ 和 $y$，$x<=y$，它们的范围都在$1000$到$9999$之间，求 $x$ 和 $y$ 之间有多少个回文数。

**回文数**是指：从左往右读，和从右往左读 是一样的。        
        
例如：$1221$、$6666$ 都是回文数

## 输入格式

两个正整数 $x$ 和 $y$，中间有一个空格。

## 输出格式

一个正整数，表示 $x$ 和 $y$之间回文数的数量。

## 样例 #1

### 样例输入 #1

```
1003    1009
```

### 样例输出 #1

```
0
```

## 样例 #2

### 样例输入 #2

```
1001    1001
```

### 样例输出 #2

```
1
```

## 样例 #3

### 样例输入 #3

```
1000    9999
```

### 样例输出 #3

```
90
```

## 提示

本题是横向的输入方式，请用下面的方法：   
s=input().split()    
x=int(s[0])    
y=int(s[1])   


说明：input进入电脑的是一个字符串，用split函数切割为一个列表s，然后从列表里取出各个数字，列表元素的编号是从0开始的。
"""

s = input().split()
x = int(s[0])
y = int(s[1])

k = 0

for i in range(x, y + 1):
    if 1000 <= i <= 9999 and i % 11 == 0:
        d = i % 10
        r = i // 11 - 91 * d
        if r % 10 == 0 and 0 <= r <= 90:
            k += 1

print(k)
