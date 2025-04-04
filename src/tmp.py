# 복습 - 점프
# https://www.acmicpc.net/problem/1890

# O(N^2)

dx = [1, 0]
dy = [0, 1]

import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] != 0 and data[i][j] != 0:
            for k in range(2):
                new_i = i + data[i][j] * dx[k]
                new_j = j + data[i][j] * dy[k]
                if 0 <= new_i < n and 0 <= new_j < n:
                    dp[new_i][new_j] += dp[i][j]


print(dp[-1][-1])