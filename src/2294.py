# 동전 2
# https://www.acmicpc.net/problem/2294
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline
INF = int(1e9)
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [INF] * (k+1) # idx: 금액, value: 동전 개수
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)
    
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])