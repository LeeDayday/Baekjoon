# 01타일
# https://www.acmicpc.net/problem/1904
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

if n <= 2:
    print(n)
    exit(0)

dp = [0] * (n+1)
dp[1] = 1 # 1
dp[2] = 2 # 00, 11

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[-1])