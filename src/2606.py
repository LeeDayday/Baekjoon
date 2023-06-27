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

def dfs(v):
    global cnt
    visited.append(v)

    for i in range(n):
        if graph[v][i]:
            if i not in visited:
                dfs(i)
                cnt += 1

cnt = 0
dfs(0)
print(cnt)