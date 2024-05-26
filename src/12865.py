# 평범한 배낭
# https://www.acmicpc.net/problem/12865
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# i번째 (w, v) 경우에 대하여
for i in range(1, n+1):
   # 무게 j일 때 최대 value
    for j in range(k+1):
        curr_w, curr_v = data[i-1]
        if j >= curr_w:
            dp[i][j] = max(curr_v + dp[i-1][j-curr_w], dp[i-1][j])
        else:
           dp[i][j] = dp[i-1][j]

print(dp[n][k])