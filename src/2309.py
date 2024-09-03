# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
# 브루트포스 알고리즘, 정렬

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline


data = [int(input()) for _ in range(9)]

for comb in combinations(data, 7):
    if sum(comb) == 100:
        break
comb = list(comb)
comb.sort()
for num in comb:
    print(num)
