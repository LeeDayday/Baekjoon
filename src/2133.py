# 타일 채우기
# https://www.acmicpc.net/problem/2133
# 다이나믹 프로그래밍

# =======================================
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
dp = [0] * 31
dp[1] = 0
dp[2] = 3

if n <= 3:
    print(dp[n])
    exit(0)

for i in range(4, n+1):
    # 넓이가 짝수인 경우에만 타일을 채울 수 있음
    if i % 2 == 0:
        dp[i] += dp[i-2] * 3
        dp[i] += sum(dp[:i-2]) * 2
        dp[i] += 2
    
        
print(dp[n])