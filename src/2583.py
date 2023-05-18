# 영역 구하기
# https://www.acmicpc.net/problem/2583
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    start_row, start_col, end_row, end_col = map(int, sys.stdin.readline().split())

    for i in range(start_col, end_col):
        for j in range(start_row, end_row):
            graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    area = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                area += 1
    return area

cnt = 0
result = []
for i in range(0, m):
    for j in range(0, n):
        if graph[i][j] == 0:
            result.append(bfs(i, j))
            cnt += 1

print(cnt)
result.sort()
for num in result:
    print(num, end=' ')
