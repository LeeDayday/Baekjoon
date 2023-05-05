# DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 그래프 이론, 그래프 탐색, BFS, DFS

# =======================================
import sys
from collections import deque


def dfs(graph, visited, v):
    # 현재 노드 방문 처리
    visited.append(v)
    print(v, end=' ')
    # 인접 노드 방문
    for nv in graph[v-1]:
        if nv not in visited:
            dfs(graph, visited, nv)

def bfs(Queue, arr, visited):
    while len(Queue):
        v = Queue.popleft()
        for node in arr[v-1]:
            if node not in visited:
                Queue.append(node)
                visited.append(node)
        

n, m, v = map(int, sys.stdin.readline().split())

# 인접 리스트 생성
adjacency_list = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adjacency_list[x-1].append(y) # 정점 번호 추가
    adjacency_list[y-1].append(x)


for i in range(n):
    adjacency_list[i].sort()


visited = []

dfs(adjacency_list, visited, v)

print()

visited.clear()
visited.append(v)

Queue = deque()
Queue.append(v)

bfs(Queue, adjacency_list, visited)
for i in visited:
    print(i, end=' ')