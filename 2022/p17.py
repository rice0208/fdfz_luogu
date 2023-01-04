r"""
(c) 2023 by rice0208, licensed under MIT.

# 判断素数

## 题目描述

给定一个正整数 $n$ ，判断它是不是素数。

## 输入格式

$\quad$ $\quad$ 一个正整数 $n$ ，$1<=n<=999,999,999$

## 输出格式

$\quad$ $\quad$  如果 $n$ 是素数，输出 Yes ；      
$\quad$ $\quad$  如果 $n$ 不是素数，输出 No 。

## 样例 #1

### 样例输入 #1

```
1
```

### 样例输出 #1

```
No
```

## 样例 #2

### 样例输入 #2

```
23
```

### 样例输出 #2

```
Yes
```

## 样例 #3

### 样例输入 #3

```
99
```

### 样例输出 #3

```
No
```

## 样例 #4

### 样例输入 #4

```
100000007
```

### 样例输出 #4

```
Yes
```

## 样例 #5

### 样例输入 #5

```
500000009
```

### 样例输出 #5

```
Yes
```

## 提示

$n$ 的范围很大，如果不加优化，$\color{Red}\textbf{当心超时}$。
"""

# i ranges from 2 to sqrt(n), check if i is factor of n.

# 复制以下内容：

n = int(input())

if n == 1:
    print("No")
elif n == 2:
    print("Yes")
else:
    for i in range(2, n):
        if i * i > n:
            print("Yes")
            break
        if n % i == 0:
            print("No")
            break
