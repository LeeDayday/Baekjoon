# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
# dp[i][j], i: 계단 수의 길이 - 1, j: 일의 자리 수
dp = [[0 for _ in range(10)]for _ in range(n)]

# 길이가 2인 경우 값 초기화
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

print(sum(dp[-1])%1000000000)