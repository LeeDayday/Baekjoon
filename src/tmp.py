# 복습 - 최소비용 구하기
# https://www.acmicpc.net/problem/1916

from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

data = defaultdict(list)
for _ in range(m):
    start, end, weight = map(int, input().split())
    data[start].append((end, weight))

s, e = map(int, input().split())

def solution(s, e):
    distance = [float('inf')] * (n + 1) # 정점 s에서부터 다른 정점까지의 최소 거리 저장
    distance[s] = 0
    heap = []
    heappush(heap, (distance[s], s)) # 힙에 (거리, 번호) 관리
    while heap:
        curr_dist, curr_num = heappop(heap)
        if distance[curr_num] < curr_dist:
            continue
        for new_num, new_dist in data[curr_num]:
            # s -> new_num vs s -> curr_num -> new_num
            if distance[new_num] > distance[curr_num] + new_dist:
                distance[new_num] = distance[curr_num] + new_dist
                heappush(heap, (distance[new_num], new_num))


    return distance[e]

print(solution(s, e))


