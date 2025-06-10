# 진우의 달 여행 (Small)
# https://www.acmicpc.net/problem/17484
# 다이나믹 프로그래밍, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

dx = [1, 1, 1]
dy = [-1, 0, 1]


n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [[[0] * m for _ in range(n)] for _ in range(3)] # dp[i][j][k]: i 방향, data[j][k] 연료

# 초기 dp 초기화
for i in range(3):
    for k in range(m):
        dp[i][0][k] = data[0][k]

for j in range(1, n):
    for k in range(m):
        # 첫 번째 열, 마지막 열은 방향 제한 O
        if k == 0:
            dp[0][j][k] = dp[1][j - 1][k]
            dp[1][j][k] = dp[0][j - 1][k + 1]
            dp[2][j][k] = min(dp[0][j - 1][k + 1], dp[1][j - 1][k])
        elif k == m - 1:
            dp[0][j][k] = min(dp[1][j - 1][k], dp[2][j - 1][k - 1])  
            dp[1][j][k] = dp[2][j - 1][k - 1]
            dp[2][j][k] = dp[1][j - 1][k]
        else:
            dp[0][j][k] = min(dp[1][j - 1][k], dp[2][j - 1][k - 1])  
            dp[1][j][k] = min(dp[0][j - 1][k + 1], dp[2][j - 1][k - 1]) 
            dp[2][j][k] = min(dp[0][j - 1][k + 1], dp[1][j - 1][k]) 
        for i in range(3):
            dp[i][j][k] += data[j][k]
        
answer = float('inf')
for i in range(3):
    answer = min(answer, min(dp[i][-1]))

print(answer)