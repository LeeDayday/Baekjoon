# 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    # 좌표 정보를 담는 그래프
    # [0]: 상근이네 집 좌표
    # [1 ~ n]: n개의 편의점 좌표
    # [n+1]: 락 페스티벌 좌표

    graph = []
    visited = [False] * (n+2)
    # 상근이네 집 좌표
    graph.append(list(map(int, sys.stdin.readline().split())))
    # n개의 편의점 좌표
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    # 락 페스티벌 좌표
    graph.append(list(map(int, sys.stdin.readline().split())))

    def bfs(v):
        queue = deque()
        queue.append(graph[v])
        visited[v] = True
        while queue:
            x, y = queue.popleft()
            if abs(graph[-1][0] - x) + abs(graph[-1][1] - y) <= 1000:
                visited[-1] = True
                break
            for i in range(1, n+1):
                if visited[i] is False:
                    dx = abs(x - graph[i][0])
                    dy = abs(y - graph[i][1])
                    dis = dx + dy
                    if dis <= 1000:
                        visited[i] = True
                        queue.append(graph[i])
                    
    bfs(0)
    if visited[-1] is True:
        print("happy")
    else:
        print("sad")