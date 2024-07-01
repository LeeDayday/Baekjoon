# 1로 만들기 2
# https://www.acmicpc.net/problem/12852
# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색

# =======================================
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
dp = [INF] * (n+1)

dp[1] = 0
for i in range(1, n+1):
    if i * 3 <= n:
        dp[i * 3] = min(dp[i*3], dp[i] + 1)
    if i * 2 <= n:
        dp[i * 2] = min(dp[i*2], dp[i] + 1)
    if i + 1 <= n:
        dp[i + 1] = min(dp[i+1], dp[i] + 1)

print(dp[n])

result = []
idx = n
while idx > 0:
    curr_dis = dp[idx]
    result.append(idx)
    if idx % 3 == 0 and dp[idx//3] == curr_dis - 1:
        idx = idx // 3
    elif idx % 2 == 0 and dp[idx//2] == curr_dis - 1:
        idx = idx // 2
    else:
        idx -= 1
print(*result)