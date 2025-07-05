# 택배 배송
# https://www.acmicpc.net/problem/5972
# 그래프 이론, 최단 경로, 데이크스트라

# =======================================
import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 헛간의 개수, m: 소가 다니는 길의 개수

data = defaultdict(list)
for _ in range(m):
    start, end, weight = map(int, input().split())
    data[start].append((end, weight))
    data[end].append((start, weight))

weight = [float('inf')] * (n + 1) # 정점 1에서 다른 정점까지의 최단 비용
def dijkstra(start, end):
    weight[start] = 0
    heap = []

    heappush(heap, (weight[start], start))

    while heap:
        curr_weight, curr_node = heappop(heap)
        # 갱신 필요 여부 검사
        if weight[curr_node] < curr_weight:
            continue
        for next_node, next_weight in data[curr_node]:
            if weight[next_node] > curr_weight + next_weight:
                heappush(heap, (curr_weight + next_weight, next_node))
                weight[next_node] = curr_weight + next_weight

dijkstra(1, n)
print(weight[-1])