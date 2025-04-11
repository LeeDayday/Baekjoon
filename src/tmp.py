# 복습 - 괄호
# https://www.acmicpc.net/problem/10422

# O(n^2)

import sys
input = sys.stdin.readline

dp = [0] * (5001)
dp[0] = 1
dp[2] = 1

for i in range(4, 5001, 2):
    for j in range(0, i, 2):
        dp[i] += dp[j] * dp[i - j - 2]
        dp[i] %= 1000000007

for _ in range(int(input())):
    l = int(input())
    if l % 2:
        print(0)
    else:
        print(dp[l])