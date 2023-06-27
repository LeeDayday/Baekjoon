# 바이러스
# https://www.acmicpc.net/problem/2606
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0 for i in range(n)] for i in range(n)]
visited = []

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1

def bfs(v):
    cnt = 0
    queue = deque()
    queue.append(v)
    visited.append(v)

    while queue:
        v = queue.popleft()
        cnt += 1

        for i in range(n):
            node = graph[v][i]
            
            if node:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
    return cnt

print(bfs(0)-1)