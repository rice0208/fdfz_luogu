r"""
(c) 2023 by rice0208, licensed under MIT.

# 十进制转二进制

## 题目背景

输入一个正整数 $n$，请将它转换为二进制后输出。

## 题目描述

## 输入格式

## 输出格式

## 样例 #1

### 样例输入 #1

```
1
```

### 样例输出 #1

```
1
```

## 样例 #2

### 样例输入 #2

```
13
```

### 样例输出 #2

```
1101
```

## 样例 #3

### 样例输入 #3

```
63
```

### 样例输出 #3

```
111111
```

## 样例 #4

### 样例输入 #4

```
64
```

### 样例输出 #4

```
1000000
```

## 样例 #5

### 样例输入 #5

```
99
```

### 样例输出 #5

```
1100011
```

## 提示

输出的时候，数字中间不要加空格，Python语言中不换行输出的实现方法是在print函数中加参数end=''。     
例如，想输出21，可以写成：    
print(2,end='')    
print(1,end='')
"""

n = int(input())
a = []

while n > 1:
    a.append(n % 2)
    n //= 2

print(1, end="")

for i in range(1, len(a) + 1):
    print(a[len(a) - i], end="")
