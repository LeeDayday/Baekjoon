# 복습 - 평범한 배낭
# https://www.acmicpc.net/problem/12865

# O(nk)

import sys
input = sys.stdin.readline

n, k  = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [0] * (k + 1)

for w, v in data:
    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)


print(dp[-1])