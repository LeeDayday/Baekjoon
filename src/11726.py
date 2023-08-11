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
def sol(i, dp):
    if dp[i-1] == 0:
        sol(i-1, dp)
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

if n > 2:
    sol(n, dp)
print(dp[n])