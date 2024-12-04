# 1학년
# https://www.acmicpc.net/problem/5557
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline


n = int(input())
data = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(n - 1)]
dp[0][data[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if j - data[i] >= 0:
            dp[i][j - data[i]] += dp[i - 1][j]
        if j + data[i] <= 20:
            dp[i][j + data[i]] += dp[i - 1][j]

print(dp[-1][data[-1]])