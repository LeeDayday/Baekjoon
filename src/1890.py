# 점프
# https://www.acmicpc.net/problem/1890
# 다이나믹 프로그래밍

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        step = graph[i][j]
        if step == 0:
            continue
        if i + step < n:
            dp[i + step][j] += dp[i][j]
        if j + step < n:
            dp[i][j + step] += dp[i][j]


print(dp[-1][-1])