# 복습 - 퇴사 2
# https://www.acmicpc.net/problem/15486

# O(N)

import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [0] * (n + 1) # (i - 1)일에 얻을 수 있는 최대 수익

for i in range(n):
    # 오늘 상담을 하는 경우
    if i + data[i][0] <= n:
        dp[i + data[i][0]] = max(dp[i + data[i][0]], dp[i] + data[i][1])

    # 최대 수익 반영
    dp[i + 1] = max(dp[i + 1], dp[i])    

print(dp[-1])
