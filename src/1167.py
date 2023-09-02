# 트리의 지름
# https://www.acmicpc.net/problem/1167
# 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [False for _ in range(v+1)]    
    visited[start] = True
    # max_len: 정점 번호 start 를 기준으로 다른 정점까지의 거리
    max_len = [0 for _ in range(v+1)]

    while queue:
        num = queue.popleft()
        # 정점 번호 num의 인접 리스트 순환
        for node_num, cost in edge[num]:
            # num과 인접한 정점 중 미방문 정점이 있다면
            if visited[node_num] is False:
                max_len[node_num] = max(max_len[node_num], max_len[num] + cost)
                queue.append(node_num)
                visited[node_num] = True

    max_i = 1
    max_d = 0 
    for i in range(1, v+1):
        if max_d < max_len[i]:
            max_i = i
            max_d = max_len[i]

    return max_i, max_d

# v: 트리 정점의 개수
v = int(input())

# edge: 인접 리스트
edge = [[] for _ in range(v+1)] # idx 1부터 유의미한 값
for _ in range(v):
    edge_info = tuple(map(int, input().split()))
    start = edge_info[0]
    for idx in range(1, len(edge_info), 2):
        end = edge_info[idx]
        if end == -1:
            break
        edge[start].append((end, edge_info[idx+1]))

max_d = 0
# 첫 번째 bfs 수행: 1번 정점에서 가장 먼 정점(num)을 구한다
num, d = bfs(1)

# 두 번째 bfs 수행: (num)번 정점에서 가장 먼 정점을 구한다
num, d = bfs(num)
print(d)

    

