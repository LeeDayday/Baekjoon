# 동전 1
# https://www.acmicpc.net/problem/2293
# 다이나믹 프로그래밍

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1) # idx: 금액, value: 해당 금액을 만들 수 있는 경우의 수
dp[0] = 1 # 0원을 만들 수 있는 경우의 수: 1가지 (동전을 모두 사용하지 않는 경우)

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])