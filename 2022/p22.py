r"""
(c) 2023 by rice0208, licensed under MIT.

# 低洼地

## 题目描述

一组数，分别表示地平线的高度变化。高度值为整数，相邻高度用直线连接。找出并统计有多少个可能积水的低洼地？

如图：地高变化为 0 1 0 2 1 2 0 0 2 0





![](https://cdn.luogu.com.cn/upload/pic/116.png)

## 输入格式

两行，第一行n,表示有n个数。第2行连续n个数表示地平线高度变化的数据，保证首尾为0。(3<=n<=10000,0<=高度<=1000)

## 输出格式

一个数，可能积水低洼地的数目。

## 样例 #1

### 样例输入 #1

```
10
0 1 0 2 1 2 0 0 2 0
```

### 样例输出 #1

```
3
```

## 提示

本题需要用到列表    
在Python语言中，横向输入的方法是：    
x=input().split()
"""

x = int(input())
y = input().split()

a = 0
t = []

for i in range(x - 1):
    if int(y[i]) != int(y[i - 1]):
        t.append(y[i])

for i in range(1, len(t) - 1):
    if int(t[i]) < int(t[i - 1]) and int(t[i]) < int(t[i + 1]):
        a += 1

print(a)
