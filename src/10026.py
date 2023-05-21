# 적록색약
# https://www.acmicpc.net/problem/10026
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque

n = int(sys.stdin.readline())

graph = []

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, flag):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    color = graph[x][y]

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            ncolor = graph[nx][ny]

            if flag == 1 and color != 'B' and ncolor != 'B':
                ncolor = color

            if ncolor == color and visited[nx][ny] is False:
                queue.append((nx, ny))
                visited[nx][ny] = True

# 적록 색약 x
non_cnt = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            bfs(i, j, visited, 0)
            non_cnt += 1

# 적록 색약 o
cnt = 0

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            bfs(i, j, visited, 1)
            cnt += 1

print(non_cnt, cnt)