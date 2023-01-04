# FDFZ Luogu

[![MIT License](https://shields.io/github/license/rice0208/fdfz_luogu)](https://github.com/rice0208/fdfz_luogu/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[README in English](https://github.com/rice0208/fdfz_luogu/blob/master/README.md)

这里存放着复旦附中在 [洛谷](https://www.luogu.com.cn) 网站上布置的程序设计作业的答案。

## 为什么要创建这个 repo？

最近有很多同学来问过我关于这份洛谷作业的问题。为了方便起见，我决定将所有的答案上传到这个 repo，这样所有的答案都可以公开，而不需要使用私聊分别发送。

另外这个 repo 也相当于存储了我的作业答案，这样如果哪天我需要它们我可以直接上 GitHub 找而不是到洛谷去点各种链接才能找到。

## 使用说明

如果你想要将这个 repo 的内容复制到你的洛谷作业，请遵守以下步骤：

**Step 1** 在最下方的列表中找到你想要复制的问题。例如「游泳时间」是序号 1。

**Step 2** 打开目录 /2022，并找到与序号对应的文件（例如：序号 1 对应 p01.py）。复制源代码中的程序部分。例如对于序号 1 的程序，你只需要复制注释以外的内容（不然一看就知道是抄的 ^.^）：

```python
a = int(input())
b = int(input())
c = int(input())
d = int(input())

m = ((c - a) * 60 + (d - b))

print(m // 60, m % 60)
```

**Step 3** 把答案粘贴到洛谷。由于这个 repo 根据的许可证是 MIT License（licensed under MIT），所以你怎么复制都没有问题。

**Step 4** 稍微修改一下答案。我想你我应该**都不希望有老师发现作业是抄答案的**。

## 这个 repo 有什么？

根据复旦附中 2022 程序设计课程中高一 4 班的作业里各题顺序依次排列，其它的题目附加在列表底部（如「应读尽读」）

1. 游泳时间
2. 分解四位数
3. 交换两个变量的值
4. 判断四位回文数
5. 判断三角形的类型
6. 某年某月的天数
7. 解方程
8. 吃苹果
9. 正方形操场
10. 数列求和
11. 打印因子--III
12. 尼科彻斯定理
13. 四位回文数的数量
14. Beautiful Year
15. 找最小值
16. 电源拖线板
17. 判断素数
18. 百鸡问题
19. 小明的秘密操场
20. 陶陶摘苹果
21. 统计天数
22. 低洼地
23. 校门外的树
24. 校门外的鸟
25. 草料拍卖
26. 数字反转
27. 十进制转二进制
28. 冰雹猜想
29. 最大公因数
30. 应读尽读

## 关于这个 repo 的 contribution

欢迎对这个 repo 中的内容提出 issue 或者 PR。
