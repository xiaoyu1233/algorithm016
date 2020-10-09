from fractions import Fraction
import collections
res = collections.defaultdict(int)
rows = int(input())
matrix = []
res = {}
for i in range(rows):
    line = list(map(int, input().split()))
    num_1 = sum(line)
    num_all = len(line)
    val = Fraction(num_1, num_all)
    res[i+1] = val
print(res)

# # coding=utf-8
# from fractions import Fraction
# numerator = 2  # 分子
# denominator = 6  # 分母bai
# print(Fraction(numerator, denominator))