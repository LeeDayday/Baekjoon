# 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-워셜

# =======================================
import sys
from collections import deque
from math import inf
input = sys.stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)
    visited = [False for _ in range(n)] 
    bacon = [0 for _ in range(n)]
    while queue:
        node = queue.popleft()
        # neighbor_num은 node idx가 아니라 학생 번호 (-1 해야 idx로 접근 가능)
        for neighbor_num in graph[node]:
            if visited[neighbor_num-1] is False:
                queue.append(neighbor_num-1)
                bacon[neighbor_num-1] = bacon[node] + 1
                visited[neighbor_num-1] = True
    return sum(bacon)

n, m = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1].append(y)
    graph[y-1].append(x)

min_bacon = inf
min_num = 1
# bfs는 학생 번호가 아닌 idx를 기준으로 수행한다
for i in range(n):
    result = bfs(i)
    if min_bacon > result:
        min_bacon = result
        min_num = i + 1

print(min_num)