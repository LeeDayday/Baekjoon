# 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485
# 그래프 이론, 그래프 탐색, 최단 경로, 데이크스트라, 격자 그래프

# =======================================
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution(data, n):
    distances = [[float('inf')] * n for _ in range(n)]
    heap = []
    distances[0][0] = data[0][0]
    heappush(heap, (distances[0][0], 0, 0))

    while heap:
        curr_dist, i, j = heappop(heap)
        if distances[i][j] < curr_dist:
            continue
        for x in range(4):
            new_i = i + dx[x]
            new_j = j + dy[x]
            if 0 <= new_i < n and 0 <= new_j < n:
                if distances[new_i][new_j] > curr_dist + data[new_i][new_j]:
                    distances[new_i][new_j] = curr_dist + data[new_i][new_j]
                    heappush(heap, (curr_dist + data[new_i][new_j], new_i, new_j))

    return distances[-1][-1]

step = 1
while True:
    n = int(input())
    if n == 0:
        break
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    
    print(f"Problem {step}: {solution(data, n)}")
    step += 1