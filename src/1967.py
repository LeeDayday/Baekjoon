# 트리의 지름
# https://www.acmicpc.net/problem/1967
# 

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    queue = deque()
    queue.append(num)
    visited = [False for _ in range(n+1)]
    visited[num] = True

    max_list = [0 for _ in range(n+1)]
    while queue:
        num = queue.popleft()
        for node, weight in graph[num]:
            if visited[num] is False:
                queue.append(node)
                visited[node] = True
                max_list[node] = weight
n = int(input())
graph = [[]for _ in range(n+1)]

for _ in range(n-1):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

