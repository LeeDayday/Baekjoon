# 복습 - 덩치
# https://www.acmicpc.net/problem/7568

# O(N^2)

import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int ,input().split())))

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j:
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                rank += 1
    print(rank, end=' ')
