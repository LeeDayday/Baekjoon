# 아기 상어 2
# https://www.acmicpc.net/problem/17806
# 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [0, 1, -1, 1, -1, 0, 1, -1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(graph, i, j):
    queue = deque()
    queue.append((i, j, 0))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[i][j] = True
    while queue:
        curr_x, curr_y, curr_distance = queue.popleft()
        for i in range(8):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < m:
                if visited[new_x][new_y] is False:
                    if graph[new_x][new_y] == 1:
                        return curr_distance + 1
                    queue.append((new_x, new_y, curr_distance + 1))
                    visited[new_x][new_y] = True

    return 0


max_result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            max_result = max(max_result, bfs(graph, i, j))

print(max_result)