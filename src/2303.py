# 극장 좌석
# https://www.acmicpc.net/problem/2302
# 다이나믹 프로그래밍

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input()) # 고정석 개수

vip = [int(input()) for _ in range(m)]

dp = [0] * (41)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(n)
total = 1
start = 1
print(dp)
for end in vip: # cnt 범위: [start, end)
    cnt = end - start
    total *= dp[cnt]
    start = end + 1

if start <= n: # cnt 범위: [start, n]
    cnt = n - start + 1
    total *= dp[cnt]

print(total)
