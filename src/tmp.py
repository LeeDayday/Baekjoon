# 복습 - 1학년
# https://www.acmicpc.net/problem/5557

# O(N)

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n - 1)]

dp[0][data[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j] != 0:
            if 0 <= j - data[i] <= 20:
                dp[i][j - data[i]] += dp[i - 1][j]
            if 0 <= j + data[i] <= 20:
                dp[i][j + data[i]] += dp[i - 1][j]

print(dp[-1][data[-1]])