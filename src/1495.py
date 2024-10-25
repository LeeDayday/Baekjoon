# 기타리스트
# https://www.acmicpc.net/problem/1495
# 다이나믹 프로그래밍

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

# p + v[i], p - v[i]로 연주
# 0 <= 볼륨 크기 <= m
dp = [[False] * (m + 1) for _ in range(n + 1)]
queue = deque()
queue.append((0, s)) # 곡 0, 시작 볼륨 s
dp[0][s] = True

while queue:
    idx, volume = queue.popleft()
    if idx == n: # 모든 곡을 마친 경우
        continue

    next_volume = volume + v[idx]
    if next_volume <= m and dp[idx + 1][next_volume] is False:
        dp[idx + 1][next_volume] = True
        queue.append((idx + 1, next_volume))
    
    next_volume = volume - v[idx]
    if next_volume >= 0 and dp[idx + 1][next_volume] is False:
        dp[idx + 1][next_volume] = True
        queue.append((idx + 1, next_volume))

# 마지막 곡(n번째)의 가능한 최대 볼륨 찾기
result = -1
for volume in range(m + 1):
    if dp[n][volume]:
        result = max(result, volume)

print(result)
