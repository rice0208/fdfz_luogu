r"""
(c) 2023 by rice0208, licensed under MIT.

# 冰雹猜想

## 题目描述

给出一个正整数 $n$，然后对这个数字一直进行下面的操作：如果这个数字是奇数，那么将其乘 $3$ 再加 $1$，否则除以 $2$。经过若干次循环后，最终都会回到 $1$。经过验证很大的数字（$7\times10^{11}$）都可以按照这样的方式比变成 $1$，所以被称为“冰雹猜想”。例如当 $n$ 是 $20$，变化的过程是 $20\to 10\to 5\to 16\to 8\to 4\to 2\to 1$。

根据给定的数字，验证这个猜想，并从最后的 $1$ 开始，倒序输出整个变化序列。

## 输入格式

输入一个正整数 $n$。

## 输出格式

输出若干个由空格隔开的正整数，表示从最后的 $1$ 开始倒序的变化数列。

## 样例 #1

### 样例输入 #1

```
20
```

### 样例输出 #1

```
1 2 4 8 16 5 10 20
```

## 提示

数据保证，$1 \le n\le 100$。     
Python语言在输出的时候，两个数据中间有一个空格同时又不换行的写法是print(数据，end=' ')，引号中间有一个空格。
"""

a = int(input())

l = []

while a != 1:
    l.append(str(a))
    if a % 2 == 0:
        a = a // 2
    else:
        a = a * 3 + 1

l.append(1)

for i in range(1, len(l)):
    print(l[len(l) - i], end=" ")

print(l[0])
