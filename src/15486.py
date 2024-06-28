# 퇴사 2
# https://www.acmicpc.net/problem/15486
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [0] * (n + 1) # idx 일 이후의 최대 이익
max_value = 0
for i in range(n - 1, -1, -1):
    time = i + data[i][0]
    if time > n:
        dp[i] = max_value
    else:
        dp[i] = max(dp[time] + data[i][1], max_value)
        max_value = dp[i]
        
print(max_value)