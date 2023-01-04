r"""
(c) 2023 by rice0208, licensed under MIT.

# 草料拍卖

## 题目描述

农夫FDFZ的干草又丰收了，但是因为学生们的节食运动，给 FDFZ 余下了一大批干草无法处理，所以他准备要开一个拍卖会，对外出售他的干草。

他有 $n$ 批干草，他的客户有 $m$ 个，都是和他相邻的农夫。第 $i$ 名农夫会告诉 FDFZ 为每批干草付 $p_i$ 的钱。每个农夫都想买（也只想买）FDFZ 的一批草料。

为了确保农夫们不会互相嫉妒，所以 FDFZ 决定要以一个固定的价格出售他的草料。每一个出价比 FDFZ 的要价要高的农夫将会买到草料，余下的将会被拒绝购买。

请你帮助 FDFZ 找出能让他赚到最多的钱的最低的单批草料的售价。

## 输入格式

第一行：两个被空格隔开的整数，$n$ 和 $m$。

第二行到第 $m+1$ 行：第 $i+1$ 行只包含一个整数：$p_i$。

## 输出格式

共一行，包含由空格隔开的两个整数：FDFZ 能出的每批草料的最低价格，以及他能赚到的最多的钱。

## 样例 #1

### 样例输入 #1

```
5 4
2
8
10
7
```

### 样例输出 #1

```
7 21
```

## 样例 #2

### 样例输入 #2

```
10 8
4
2
1
7
9
6
5
3
```

### 样例输出 #2

```
4 20
```

## 提示

对于样例一：FDFZ 有 $5$ 批草料，$4$ 个农夫想要购买。他们出价分别为：每批草料为 $2$，$8$，$10$ 和 $7$。

FDFZ 应该把价格设定为 $7$，这样会有 $3$ 个农夫会付钱买草料，FDFZ 自己会挣到 $7*3=21$ 。    
      
对于样例二：按照从大到小排序后，选前4个或前5个，总盈利都是20，但题目要求售价尽可能低，所以应该选5个，单价是4。
"""

# nm = input().split()
# p = []
# ans = 0
# for i in range(1, int(nm[1]) + 1):
#     p.append(int(input()))
#
# p.sort()
# q = 0
#
# for j in range(len(p)):
#     if len(p) - j <= int(nm[0]):
#         t = p[j] * (len(p) - j)
#     else:
#         t = p[j] * (int(nm[0]))
#     if ans < t:
#         ans = t
#         q = p[j]
#         h = len(p) - j
#
# print(q, ans)

# solution above called list.sort() method,
# which is not recommended in python algorithm.

# 复制以下内容：

nm = input().split()
n = int(nm[0])
m = int(nm[1])

p = []
for _ in range(m):
    p.append(int(input()))

incomes = []
for i in p:
    affordable = 0
    for j in p:
        if j >= i:
            affordable += 1
    if affordable > n:
        continue
    incomes.append([i, affordable*i])

ans2 = 0
for i in incomes:
    if i[1] > ans2:
        ans2 = i[1]

max_prices = []
for i in incomes:
    if i[1] == ans2:
        max_prices.append(i[0])

ans1 = max_prices[0]
for i in max_prices:
    if i < ans1:
        ans1 = i

print(ans1, ans2)
