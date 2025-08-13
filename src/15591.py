# MooTube (Silver)
# https://www.acmicpc.net/problem/15591

# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# n: 동영상 개수, questions: 질문 개수
n, questions = map(int, input().split())
graph = defaultdict(list)

for _ in range(n - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

def bfs(k: int, v: int) -> int:
    visited = [False] * (n + 1)
    visited[v] = True
    cnt = 0
    queue = deque([v])

    while queue:
        node = queue.popleft()
        for new_node, new_weight in graph[node]:
            if not visited[new_node] and new_weight >= k:
                visited[new_node] = True
                cnt += 1
                queue.append(new_node)
    return cnt

for _ in range(questions):
    k, v = map(int, input().split())
    print(bfs(k, v))
