# 이친수
# https://www.acmicpc.net/problem/2193
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

if n < 2:
    print(1)
else:
    dp = [0] * n 
    # 자릿수가 1인 경우 (1)
    dp[0] = 1
    # 자릿수가 2인 경우 (10)
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[-1])