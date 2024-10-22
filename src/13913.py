# 숨바꼭질 4
# https://www.acmicpc.net/problem/13913
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n, k = map(int, input().split())

dist = [INF] * (100001) # 정점 n 기준 다른 정점(idx)까지 가는데 걸리는 시간
parents = [-1] * (100001) # 각 idx에 대한 부모 정점 저장

# n번 정점에서 시작
dist[n] = 0
queue = deque([n])

def move(curr_node, new_node, dist, parents):
    if new_node < 0 or new_node > 100000:
        return
    # 업데이트가 필요한 경우
    if dist[new_node] > dist[curr_node] + 1:
        dist[new_node] = dist[curr_node] + 1
        parents[new_node] = curr_node
        queue.append(new_node)
        

while queue:
    curr_node = queue.popleft()
    if curr_node == k:
        break
    # +1
    move(curr_node, curr_node + 1, dist, parents)
    # -1
    move(curr_node, curr_node - 1, dist, parents)
    # *2 이동
    move(curr_node, curr_node * 2, dist, parents)

result = []
tmp = k
while tmp != -1:
    result.append(tmp)
    tmp = parents[tmp]

print(dist[k])
print(*(result[::-1]))