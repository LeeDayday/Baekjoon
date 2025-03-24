# 복습 - DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m, v = map(int, input().split())
data = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

for key in data:
    data[key].sort()
def dfs():
    visited = [False] * (n + 1)
    stack = [v]
    answer = []
    while stack:
        curr_node = stack.pop()
        if not visited[curr_node]:
            answer.append(curr_node)
            visited[curr_node] = True
            for new_node in reversed(data[curr_node]):
                if not visited[new_node]:
                    stack.append(new_node)
    return answer

def bfs():
    visited = [False] * (n + 1)
    queue = deque([v])
    answer = []
    while queue:
        curr_node = queue.popleft()
        if not visited[curr_node]:
            visited[curr_node] = True
            answer.append(curr_node)
            for new_node in data[curr_node]:
                if not visited[new_node]:
                    queue.append(new_node)
    return answer

print(*dfs())
print(*bfs())