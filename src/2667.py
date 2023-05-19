# 단지 번호 붙이기
# https://www.acmicpc.net/problem/2667
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] != 0:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return cnt

cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            cnt += 1
            result.append(bfs(i, j))

result.sort()

print(cnt)
for num in result:
    print(num)