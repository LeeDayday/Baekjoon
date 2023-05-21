# 안전 영역
# https://www.acmicpc.net/problem/2468
# 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque
n = int(sys.stdin.readline())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

min_limit = 100
max_limit = 0

for i in range(n):
    min_row = min(graph[i])
    max_row = max(graph[i])
    min_limit = min(min_limit, min_row)
    max_limit = max(max_limit, max_row)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, height, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] > height and visited[nx][ny] is False:
                visited[nx][ny] = True
                queue.append((nx, ny))


result = 0
for height in range(min_limit, max_limit+1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 안전한 영역이면
            if graph[i][j] > height and visited[i][j] is False:
                bfs(i, j, height, visited)
                cnt += 1
    result = max(result, cnt)
print(result)
if result:
    print(result)
# 배열의 모든 값이 같은 경우 (모두 안전하거나, 모두 잠기거나)
else: 
    print(1)