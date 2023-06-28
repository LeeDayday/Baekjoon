# 촌수계산
# https://www.acmicpc.net/problem/2644
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

def dfs(v, cnt):
    cnt += 1
    visited[v] = cnt
    for i in range(n):
        if graph[v][i]:
            if visited[i] == 0:
                dfs(i, cnt)  

visited[a-1] = 1
dfs(a-1, 0)


print(visited[b-1]-1)
