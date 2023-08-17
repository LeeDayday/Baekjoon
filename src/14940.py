# 쉬운 최단거리
# https://www.acmicpc.net/problem/14940
# 

# =======================================
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # graph의 범위를 벗어나는 경우 진행 x
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 다음 인접한 영역이 아직 계산되어 있지 않고
            if visited[nx][ny] == False:
                # 접근 가능한 영역인 경우
                if graph[nx][ny] != 0:
                    # queue에 추가
                    queue.append((nx, ny))
                    # 거리 계산
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = True

n, m = map(int, input().split()) # 세로, 가로 입력

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))    

# visited: 목적지까지 계산 완료 여부 판단
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 목표 지점을 기준으로 bfs 수행
flag = 0
for i in range(n):
    if flag:
        break
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            flag = 1
            break

# bfs으로 도달하지 못한 구역은 -1로 처리
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            graph[i][j] = -1

for i in range(n):
    print(*graph[i])