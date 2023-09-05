# 최소비용 구하기
# https://www.acmicpc.net/problem/1916
# 그래프 이론, 데이크스트라

# =======================================
import sys
from math import inf
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
    min_cost = [inf for _ in range(n+1)]
    heap = []
    
    min_cost[start] = 0
    heappush(heap, [0, start])

    while heap:
        curr_cost, curr_node = heappop(heap)
        # 최소 비용을 갱신할 필요가 있는지
        if min_cost[curr_node] < curr_cost:
            continue

        for node, cost in graph[curr_node]:
            if curr_cost + cost < min_cost[node]:
                min_cost[node] = curr_cost + cost
                heappush(heap, [curr_cost + cost, node])

    return min_cost         

n = int(input())
m = int(input())

# 인접 리스트
graph = [[] for _ in range(n+1)] # idx 1부터 유의미한 값

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

s, e = map(int, input().split())

visited = [False for _ in range(n+1)]

result = dijkstra(s)
print(result[e])
