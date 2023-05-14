# 그림
# https://www.acmicpc.net/problem/1926
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
from collections import deque
import sys
# BFS 풀이

def BFS(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0
    s = 1 # 초기 넓이
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[ny][nx] == 1:
                # 방문 처리
                graph[ny][nx] = 0
                # 다음에 방문할 노드 append
                queue.append((nx, ny))
                # 넓이 늘리기
                s += 1
    
    return s



n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

max_s = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            max_s = max(max_s, BFS(j, i))
            cnt += 1

print(cnt)
print(max_s)

