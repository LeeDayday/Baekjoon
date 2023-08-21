# 파도반 수열
# https://www.acmicpc.net/problem/9461
# 수학, 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

def sol(num):
    if num <= 3:
        return 1
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n):
        if i >= 4:
            dp[i] = dp[i-1] + dp[i-5]
        else:
            dp[i] = 2
    return dp[num-1]
    

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0 for _ in range(n)]
    
    print(sol(n))
