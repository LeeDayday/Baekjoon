# 토마토
# https://www.acmicpc.net/problem/7569
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

graph = []

for i in range(h):
    tomato = []
    for j in range(n):
        tomato.append(list(map(int, sys.stdin.readline().split())))
    graph.append(tomato)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >=n or ny >= m or nz >= h:
                continue
            if graph[nz][nx][ny] == 0:
                queue.append((nx, ny, nz))
                graph[nz][nx][ny] = graph[z][x][y] + 1


queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((j, k, i))

bfs()

for i in range(h):
    for j in range(n):
        if 0 in graph[i][j]:
            print(-1)
            exit()
max_days = 0
for i in range(h):
    for j in range(n):
        max_row = max(graph[i][j])
        max_days = max(max_days, max_row)

print(max_days-1)

