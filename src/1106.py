# 호텔
# https://www.acmicpc.net/problem/1106
# 다이나믹 프로그래밍, 배낭 문제

# =======================================
import sys
input = sys.stdin.readline

c, n = map(int, input().split()) # 목표, 도시 개수
data = []
for _ in range(n):
    data.append(list(map(int, input().split()))) # 도시별 비용, 유치 고객수 입력

dp = [int(1e7)] * (c + 100)
dp[0] = 0

for cost, customers in data:
    for i in range(customers, c + 100):
        dp[i] = min(dp[i - customers] + cost, dp[i])

print(min(dp[c:]))
