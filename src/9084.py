# 동전
# https://www.acmicpc.net/problem/9084
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input()) # 동전의 가지 수
    coins = list(map(int, input().split())) # n가지 동전의 금액
    m = int(input()) # 만들어야 할 금액
    dp = [0] * (m+1)

    dp[0] = 1
    for coin in coins:
        for amount in range(coin, m + 1):
            dp[amount] += dp[amount - coin]


    print(dp[m])


