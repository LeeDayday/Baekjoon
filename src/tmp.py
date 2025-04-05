# 복습 - 기타리스트
# https://www.acmicpc.net/problem/1495

# O(nm)

import sys
from collections import deque
input = sys.stdin.readline

n, s, m = map(int, input().split())
data = list(map(int, input().split()))

answer = -1
queue = deque()
queue.append((s, 0))

visited = [[False] * (m + 1) for _ in range(n + 1)]
visited[0][s] = True # 초기 값

while queue:
    curr_volume, curr_idx = queue.popleft()
    if curr_idx == n:
        continue
    if curr_volume + data[curr_idx] <= m and not visited[curr_idx + 1][curr_volume + data[curr_idx]]:
        queue.append((curr_volume + data[curr_idx], curr_idx + 1))
        visited[curr_idx + 1][curr_volume + data[curr_idx]] = True
    if curr_volume - data[curr_idx] >= 0 and not visited[curr_idx + 1][curr_volume - data[curr_idx]]:
        queue.append((curr_volume - data[curr_idx], curr_idx + 1))
        visited[curr_idx + 1][curr_volume - data[curr_idx]] = True

for volume in range(m + 1):
    if visited[-1][volume]:
        answer = max(answer, volume)
print(answer)