# 섬의 개수
# https://www.acmicpc.net/problem/4963
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

def get_2d_graph(h):
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    return graph

def bfs(graph, i, j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0 # 방문 처리

    while queue:
        curr_i, curr_j = queue.popleft()
        for i in range(8):
            new_i = curr_i + dx[i]
            new_j = curr_j + dy[i]

            if new_i < 0 or new_i >= h:
                continue
            if new_j < 0 or new_j >= w:
                continue

            if graph[new_i][new_j] == 1:
                queue.append((new_i, new_j))
                graph[new_i][new_j] = 0

if __name__ == '__main__':
    while True:
        w, h = map(int, input().split())

        if w == 0 and h == 0:
            sys.exit(0)

        graph = get_2d_graph(h)
        
        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(graph, i, j)
                    cnt += 1
        print(cnt)