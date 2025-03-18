# 복습 - 동전 1
# https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

def solution():
    dp = [0]* (k + 1)
    dp[0] = 1
    for i in range(n):
        coin = data[i]
        for j in range(k + 1):
            if j >= coin:
                dp[j] += dp[j - coin]
        
    return dp[-1]
    
print(solution())
