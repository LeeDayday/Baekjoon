# 최단경로
# https://www.acmicpc.net/problem/1753
# 그래프 이론, 데이크스트라

# =======================================
import sys
from collections import deque
from heapq import heappop, heappush
from math import inf
input = sys.stdin.readline

def dijkstra(start):
    # 정점 k 기준. 모든 정점에 대한 최소 비용
    min_weight = [inf for _ in range(v+1)]

    # 자기 자신에 대한 비용은 0
    min_weight[start] = 0

    # 시작 노드부터 heap에 넣어 탐색 시작
    heap = []
    heappush(heap, [0, start])

    # heap이 빌 때까지 최소 비용 갱신
    while heap:
        dis, node = heappop(heap)
        # 최단 거리를 갱신할 필요가 없다면 생략
        if min_weight[node] < dis:
            continue
        for n_dis, n_node in graph[node]:
            if dis + n_dis < min_weight[n_node]:
                min_weight[n_node] = dis + n_dis
                heappush(heap, [dis + n_dis, n_node])        

    return min_weight
      

v, e = map(int, input().split())
k = int(input())

# 인접 리스트
graph = [[] for _ in range(v+1)]

for _ in range(e):
    start, end, weight = map(int, input().split())
    # 기존 입력값보다 가중치가 더 적은 경로가 있는 경우
    graph[start].append((weight, end))


result = dijkstra(k)

for i in range(1, v+1):
    if result[i] == inf:
        result[i] = "INF"

for i in range(1, v+1):
    print(result[i])
