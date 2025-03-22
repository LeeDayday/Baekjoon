# 복습 - 동전 2
# https://www.acmicpc.net/problem/2294

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

def solution():
    dp = [float('inf')] * (k + 1)
    dp[0] = 0
    for i in range(n):
        coin = data[i]
        for j in range(coin, k + 1):
            dp[j] = min(dp[j - coin] + 1, dp[j])
        
    
    if dp[-1] == float('inf'):
        return -1
    return dp[-1]
    
print(solution())
