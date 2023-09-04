# 파티
# https://www.acmicpc.net/problem/1238
# 그래프 이론, 데이크스트라

# =======================================
import sys
from math import inf
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    # start 정점을 기준. 모든 정점에 대한 최소 비용
    min_t = [inf for _ in range(n+1)]
    # start ~ start 거리는 0으로 초기화
    min_t[start] = 0

    # start 정점부터 탐색 시작
    heap = []
    heappush(heap, [0, start])

    while heap:
        t, node = heappop(heap)
        # 최소 비용 리스트를 갱신할 필요가 없다면 생략
        if min_t[node] < t:
            continue
        # 최소 비용 리스트를 최소 배용으로 갱신하기
        # node 정점의 인접리스트 탐색
        for n_node, n_t in graph[node]:
            # 최소 비용 갱신
            if t + n_t < min_t[n_node]:
                min_t[n_node] = t + n_t
                heappush(heap, [t + n_t, n_node])

    return min_t

n, m, x = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(n+1)] # idx 1부터 유의미한 값

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

result = 0
for i in range(1, n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)
