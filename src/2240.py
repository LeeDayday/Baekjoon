# 자두나무
# https://www.acmicpc.net/problem/2240
# 다이나믹 프로그래밍

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline


t, w = map(int, input().split())
data = [0] + [int(input()) for _ in range(t)]

dp = [[0 for _ in range(w + 1)] for _ in range(t + 1)]

dp[1][0] = data[1] % 2 # 1초에 1번 나무에 있는 경우
dp[1][1] = data[1] // 2 # 1초에 2번 나무에 있는 경우

for t in range(2, t+1):
    for w in range(w+1):
        if w % 2 == 0: # 1번 나무에 있는 경우
            cnt = data[t] % 2
        else:
            cnt = data[t] // 2
        dp[t][w] = max(dp[t-1][0:w+1]) + cnt
    
print(max(dp[-1]))