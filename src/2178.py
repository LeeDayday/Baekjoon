# 미로 탐색
# https://www.acmicpc.net/problem/2178
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[0][0] = 1 #

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if graph[ny][nx] == 1:
                queue.append((nx, ny))
                graph[ny][nx] = graph[y][x] + 1
                
    return graph[n-1][m-1]

print(BFS(0,0))


