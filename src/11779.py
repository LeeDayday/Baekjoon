# 최소비용 구하기 2
# https://www.acmicpc.net/problem/11779
# 그래프 이론, 최단 경로, 데이크스트라, 역추적

# =======================================
import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input()) # 도시의 개수 
m = int(input()) # 버스의 개수
data = defaultdict(list) # 출발 ~ 도착 버스 비용

for _ in range(m):
    s, e, w = map(int, input().split())
    data[s].append((e, w))
    if e not in data:
        data[e] = []

a, b = map(int, input().split()) # 구하고자 하는 구간 출발점, 도착점

visited = {key: False for key in data}
distances = {key: float('inf') for key in data}
heap = []

visited[a] = True
heappush(heap, (0, a))
answer = []
prev_node = {node: None for node in data} # prev_node = 이전 노드
distances[a] = 0
while heap:
    curr_weight, curr_node = heappop(heap)
    #if curr_node == b:
    #    break
    if distances[curr_node] < curr_weight:
        continue
    for next_node, next_weight in data[curr_node]:
        if distances[next_node] > curr_weight + next_weight:
            distances[next_node] = curr_weight + next_weight
            heappush(heap, (distances[next_node], next_node))
            prev_node[next_node] = curr_node

node = b
while node is not None:
    answer.append(node)
    node = prev_node[node]


print(distances[b]) # 최소 비용
print(len(answer)) # 경로에 포함되어있는 도시의 개수
print(*answer[::-1]) # 경로

