# 트리의 지름
# https://www.acmicpc.net/problem/1967
# 그래프 이론, 그래프 탘색, 트리, 깊이 우선 탐색

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
            if visited[node] is False:
                queue.append(node)
                visited[node] = True
                max_list[node] = max(max_list[node], max_list[num] + weight)

    max_i, max_d = 0, 0
    for idx, num in enumerate(max_list):
        if num > max_d:
            max_d = num
            max_i = idx

    return max_i, max_d
n = int(input())
graph = [[]for _ in range(n+1)]

for _ in range(n-1):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

# root 노드에서부터 가장 먼 노드 구하기
num, weight = bfs(1)
# 위에서 구한 노드로부터 가장 먼 노드 구하기 
num, weight = bfs(num)
print(weight)