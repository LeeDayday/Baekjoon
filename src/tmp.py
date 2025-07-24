# 복습 - 올림픽
# https://www.acmicpc.net/problem/8979

# O(NlogN)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
for i in range(n):
    if i > 0 and data[i][1:] != data[i - 1][1:]:
        rank = i + 1
    if data[i][0] == k:
        print(rank)
        break