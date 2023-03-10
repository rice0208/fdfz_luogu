r"""
(c) 2023 by rice0208, licensed under MIT.

# 游泳时间

## 题目描述

校际运动会要到了，小Z在拼命练习游泳准备参加游泳比赛。

这一天，小Z给自己的游泳时间做了精确的计时（本题中的计时都按24小时制计算），他发现自己从 $a$ 时 $b$ 分一直游泳到当天的 $c$ 时 $d$ 分，请你帮小Z计算一下，他这天一共游了多少时间？

## 输入格式

分4行输入，每行一个整数，分别表示 $a$, $b$, $c$, $d$ 。

## 输出格式

在一行内输出2个整数$e$和$f$，用空格分开，依次表示小鱼这天一共游了多少小时和多少分钟。    
其中表示分钟的整数 $f$ 应该小于60。

## 样例 #1

### 样例输入 #1

```
12
50
19
10
```

### 样例输出 #1

```
6  20
```

## 提示

注意： $b$<=60,   $d$<=60,   $f$<60
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

m = (c - a) * 60 + (d - b)

print(m // 60, m % 60)
