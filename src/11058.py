# 크리보드
# https://www.acmicpc.net/problem/11058
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1  # 기본: 이전 단계 + A 누르기
    for j in range(1, i - 2):
        dp[i] = max(dp[i], dp[j] * (i - j - 2 + 1))

print(dp[n])