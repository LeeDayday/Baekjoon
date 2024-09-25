# 전쟁 - 전투
# https://www.acmicpc.net/problem/1303
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(input().rstrip()))

def bfs(graph, i, j, color):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 'X' # 방문 처리
    
    result = 1
    while queue:
        curr_i, curr_j = queue.popleft()
        for i in range(4):
            new_i = curr_i + dx[i]
            new_j = curr_j + dy[i]
            # index가 범위 밖인 경우
            if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n:
                continue
            # 같은 병사가 아니거나, 이미 방문한 경우
            if graph[new_i][new_j] != color:
                continue
            queue.append((new_i, new_j))
            graph[new_i][new_j] = 'X'
            result  += 1
    return result ** 2


# 나의 병사 위력 합 구하기
result1 = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            result1 += bfs(graph, i, j, 'W')

# 적국의 병사 위력 합 구하기
result2 = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'B':
            result2 += bfs(graph, i, j, 'B')

print(result1, result2)