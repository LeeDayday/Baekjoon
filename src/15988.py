# 1, 2, 3 더하기 3
# https://www.acmicpc.net/problem/15988
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 1000001
dp[1] = 1 # 1
dp[2] = 2 # 1+1, 2
dp[3] = 4 # 1+1+1, 1+2, 2+1, 3
last = 4
for _ in range(t):
    n = int(input())
    if dp[n] != 0:
        print(dp[n])
        continue
    for i in range(last, n+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
    last = max(n, last)
    print(dp[n])
    
    


