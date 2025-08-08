# 복습 - 치킨 배달
# https://www.acmicpc.net/problem/15686

# O(cCm * h * m) (c: 총 치킨집 개수, m: 선택된 치킨집 개수, h: 가정집 개수)

import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

# n x n 크기의 도시
# 최대 m개의 치킨집만 운영
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

data_house = [] # 가정집 좌표 저장
data_chicken = [] # 치킨집 좌표 저장

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            data_house.append((i, j))
        elif graph[i][j] == 2:
            data_chicken.append((i, j))

# comb: 운영할 치킨집의 좌표 tuple
answer = float('inf')
for comb in combinations(data_chicken, m):
    distance = [float('inf')] * len(data_house) # 가정집 별 치킨 거리
    for i, j in comb: # i, j: 치킨집 좌표
        for x in range(len(data_house)):
            distance[x] = min(distance[x], abs(data_house[x][0] - i) + abs(data_house[x][1] - j))
    answer = min(answer, sum(distance))

print(answer)
