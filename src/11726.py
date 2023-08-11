# 2xn 타일링
# https://www.acmicpc.net/problem/11726
# 다이나믹 프로그래밍

# =======================================
from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1) # idx 1 부터 유의미한 값
dp[1] = 1

if n > 1:
    dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])