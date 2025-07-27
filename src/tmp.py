# 복습 - 퇴사
# https://www.acmicpc.net/problem/14501

# O(N)

import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [0] * (n + 1) # dp[i]: i일부터 상담을 시작할 경우 얻을 수 있는 최대 이익 (bottom-up)
max_value = 0

for i in range(n - 1, -1, -1): # i: 현재 날짜를 0-based index로 나타낸 것
    finished = (
        data[i][0] + i # finished: i일에 상담을 시작했을 때, 상담이 끝나는 날짜 (1-based day)
    )
    if finished > n: # 상담이 퇴사일(n) 을 넘기면 수행 불가
        dp[i] = max_value # [i]일의 작업을 수행할 수 없는 경우, 누적 최댓값으로 채우기
    else:
        dp[i] = max(max_value, data[i][1] + dp[finished])
        max_value = max(max_value, dp[i])

print(dp[0])
