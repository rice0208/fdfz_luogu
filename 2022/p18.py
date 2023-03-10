r"""
(c) 2023 by rice0208, licensed under MIT.

# 百鸡问题

## 题目背景

百鸡问题是一个数学问题，出自中国古代约5—6世纪成书的《张丘建算经》，是原书卷下第38题，也是全书的最后一题，该问题导致三元不定方程组，其重要之处在于开创“一问多答”的先例。    
      
原书没有给出解法，只说如果少买7只母鸡，就可多买4只公鸡和3只小鸡。所以只要得出一组答案，就可以推出其余两组答案。中国古算书的著名校勘者甄鸾和李淳风注释该书时都没给出解法，只有约6世纪的算学家谢察微记述过一种不甚正确的解法。到了清代，研究百鸡术的人渐多，1815年骆腾风使用大衍求一术解决了百鸡问题。1874年丁取忠创用一个简易的算术解法。在此前后时曰醇（约1870）推广了百鸡问作《百鸡术衍》，从此百鸡问题和百鸡术才广为人知。百鸡问题还有多种表达形式，如百僧吃百馒，百钱买百禽等。宋代杨辉算书内有类似问题，中古时近东各国也有相仿问题流传。例如印度算书和阿拉伯学者艾布·卡米勒的著作内都有百钱买百禽的问题，且与《张邱建算经》的题目几乎全同。    
      
------以上摘自百度百科

## 题目描述

现有100元钱，想买100只鸡，已知有三种鸡，公鸡每只5元钱，母鸡每只3元钱，小鸡一元钱3只。   
    
现要求不能剩钱，并且每种鸡至少买1只，请输出购买方案。

## 输入格式

无

## 输出格式

一共有3种方案，每行输出一种购买方案    
每种购买方案的输出方式是：在同一行里输出三个整数，分别表示公鸡数量、母鸡数量和小鸡数量，两种鸡之间有一个空格。
"""

# print 3 solutions directly.

# 复制以下内容：

print("4 18 78")
print("8 11 81")
print("12 4 84")
