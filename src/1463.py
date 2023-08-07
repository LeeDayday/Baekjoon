# 1로 만들기
# https://www.acmicpc.net/problem/1463
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1) # 1번 idx부터 유의미한 값 다룸

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])