# 줄 세우기
# https://www.acmicpc.net/problem/2252
# 그래프 이론, 위상 정렬, 방향 비순환 그래프

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

queue = deque()
for i in range(1, n + 1): # 진입차수가 0인 학생 queue에 저장
    if indegree[i] == 0:
        queue.append(i)

result = []
visited = [False] * (n + 1)
while queue:
    curr_num = queue.popleft()
    result.append(curr_num)
    visited[curr_num] = True

    # 진입차수 업데이트
    for adj_num in graph[curr_num]:
        indegree[adj_num] -= 1
        if indegree[adj_num] == 0:
            queue.append(adj_num)

print(*result)

