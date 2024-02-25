# 적록색약
# https://www.acmicpc.net/problem/10026
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(graph, visited, i, j, color):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        curr_i, curr_j = queue.popleft()
        for i in range(4):
            new_i = curr_i + dx[i]
            new_j = curr_j + dy[i]
            
            if new_i < 0 or new_i >= n:
                continue
            if new_j < 0 or new_j >= n:
                continue
            if not visited[new_i][new_j] and graph[new_i][new_j] in color:
                queue.append((new_i, new_j))
                visited[new_i][new_j] = True

if __name__ == '__main__':
    n = int(input())
    graph = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    for _ in range(n):
        graph.append(input().rstrip())

    # 적록색약이 아닌 사람
    cnt_non = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(graph, visited, i, j, graph[i][j])
                cnt_non += 1
    
    # 방문 리스트 초기화
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    # 적록색약인 사람
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] != 'B':
                bfs(graph, visited, i, j, ['R', 'G'])
                cnt += 1
            if not visited[i][j] and graph[i][j] == 'B':
                bfs(graph, visited, i, j, 'B')
                cnt += 1               
    
    print(cnt_non, cnt)