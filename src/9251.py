# LCS
# https://www.acmicpc.net/problem/9251
# 다이나믹 프로그래밍, 문자열

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline

data1 = ' ' + input().rstrip()
data2 = ' ' + input().rstrip()
# 문자열 1, 2 각각의 i, j번째 글자까지의 LCS
dp = [[0 for _ in range(len(data2))] for _ in range(len(data1))]


for i in range(1, len(data1)):
    for j in range(1, len(data2)):
        if data1[i] == data2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(dp[-1]))
