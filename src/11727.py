# 2xn 타일링 2
# https://www.acmicpc.net/problem/11727
# 

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)] # idx 1 부터 유의미한 값

if n > 2:
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-1] * dp[1]) + (dp[i-2] * (dp[2]-1))
else:
    dp[1] = 1
    if n == 2:
        dp[2] = 3

print(dp[n]%10007)
