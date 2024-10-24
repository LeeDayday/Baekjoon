# 1, 2, 3 더하기 4
# https://www.acmicpc.net/problem/15989
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

dp = [1] * (10001)

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    print(dp[n])