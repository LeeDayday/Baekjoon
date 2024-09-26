# 음식물 피하기
# https://www.acmicpc.net/problem/1743
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

def bfs(graph, i, j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0 # 방문 처리
    cnt = 1

    while queue:
        curr_i, curr_j = queue.popleft()
        for i in range(4):
            new_i = curr_i + dx[i]
            new_j = curr_j + dy[i]
            if new_i < 0 or new_j < 0 or new_i >= n or new_j >= m:
                continue
            if graph[new_i][new_j] == 1:
                graph[new_i][new_j] = 0
                cnt += 1
                queue.append((new_i, new_j))
    return cnt


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result = max(result, bfs(graph, i, j))

print(result)