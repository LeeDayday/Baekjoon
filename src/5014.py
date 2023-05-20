# 스타트링크
# https://www.acmicpc.net/problem/5014
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

# 최고층, 현재 층, 목표 층, 위로 u층 이동, 아래로 d층 이동
f, s, g, u, d = map(int, sys.stdin.readline().split())

floors = [0] * f

move = [u, -d]

def bfs(idx):
    queue = deque()
    queue.append(idx)
    floors[idx] = 1

    while queue:
        idx = queue.popleft()

        if idx == g-1:
            break
        for i in range(2):
            nidx = idx + move[i]

            if nidx < 0 or nidx >= f:
                continue

            if floors[nidx] == 0:
                floors[nidx] = floors[idx] + 1
                queue.append(nidx)
bfs(s-1)
if floors[g-1] >= 1:
    print(floors[g-1] - 1)
else:
    print("use the stairs")