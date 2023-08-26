# 헌내기는 친구가 필요해
# https://www.acmicpc.net/problem/21736
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 방문 처리
    graph[x][y] = 'V'
    # 만날 수 있는 사람 수
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 접근가능한 미방문 노드
            if graph[nx][ny] != 'V':
                if graph[nx][ny] == 'O' or graph[nx][ny] == 'P':
                    if graph[nx][ny] == 'P':
                        cnt += 1
                    queue.append((nx, ny))
                    graph[nx][ny] = 'V'
    return cnt

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))

flag = 0
for i in range(n):
    if flag:
        break
    for j in range(m):
        if graph[i][j] == 'I':
            x, y = i, j
            flag = 1
            break

result = bfs(x, y)
if result:
    print(result)
else:
    print("TT")
