# 괄호
# https://www.acmicpc.net/problem/10422
# 수학, 다이나믹 프로그래밍, 조합론

# =======================================
import sys
input = sys.stdin.readline

dp = [0] * 5001
MOD = 1000000007
dp[0] = 1
dp[2] = 1 

for i in range(4, 5001, 2):
    for j in range(0, i, 2):
        dp[i] += dp[j] * dp[i - j - 2]
        dp[i] %= MOD

for _ in range(int(input())):
    x = int(input())
    if x % 2:
        print(0)
    else:
        print(dp[x])
