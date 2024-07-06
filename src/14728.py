# 벼락치기
# https://www.acmicpc.net/problem/14728
# 다이나믹 프로그래밍, 배낭 문제

# =======================================
import sys
input = sys.stdin.readline

n, t = map(int, input().split())
data = [] # (단원 별 예상 공부 시간, 단원 문제의 배점)
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[0 for _ in range(t+1)] for _ in range(n+1)] # dp[i][j]: i번째 과목이 j시간 동안 공부했을 때 얻을 수 있는 최대 점수

for i in range(1, n+1):
    curr_time, curr_point = data[i-1]
    for j in range(1, t+1):
        if j >= curr_time:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-curr_time] + curr_point)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])