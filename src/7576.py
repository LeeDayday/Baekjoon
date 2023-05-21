# 토마토
# https://www.acmicpc.net/problem/7576
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

graph = []

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: no 토마토
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 이전 문제들과 달리 1인 위치를 append하고 bfs 시작
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()


final_day = 0

for i in range(n):
    max_row = max(graph[i])
    final_day = max(final_day, max_row)
    if 0 in graph[i]:
        print(-1)
        exit()

print(final_day-1)