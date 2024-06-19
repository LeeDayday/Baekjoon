# 가장 큰 증가하는 부분 수열
# https://www.acmicpc.net/problem/11055
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [0] * n # 각 i번째 요소를 포함하는 최대 부분 수열 합

for i in range(n):
    dp[i] = data[i]
    for j in range(i):
        if data[i] > data[j]: # 증가성을 유지하는지 확인
            dp[i] = max(dp[i], dp[j] + data[i])
print(max(dp))