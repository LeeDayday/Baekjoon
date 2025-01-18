# 안녕
# https://www.acmicpc.net/problem/1535
# 다이나믹 프로그래밍, 브루트포스 알고리즘, 배낭 문제

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
joy = list(map(int, input().split()))

dp = [[0] * (100) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(100):
        if j - l[i - 1] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - l[i - 1]] + joy[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
