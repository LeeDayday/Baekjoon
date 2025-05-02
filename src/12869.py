# 뮤탈리스크
# https://www.acmicpc.net/problem/12869
# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

n = int(input()) # scv의 개수
data = list(map(int, input().split())) # scv n개의 체력
data += [0] * (3 - n) # 3개로 맞추기

visited = [[[False] * 61 for _ in range(61)] for _ in range(61)] # dp[i][j][k]: 체력 i, j, k인 scv 상태에 도달할 때까지의 공격 횟수 + 1
visited[data[0]][data[1]][data[2]] = True
queue = deque()
queue.append((data[0], data[1], data[2], 0)) # 체력1, 체력2, 체력3, 횟수

while queue:
    x, y, z, cnt = queue.popleft()
    if x == 0 and y == 0 and z == 0:
        print(cnt)
        break
    for dx, dy, dz in permutations([9, 3, 1], 3):
        new_x = max(0, x - dx)
        new_y = max(0, y - dy)
        new_z = max(0, z - dz)
        if not visited[new_x][new_y][new_z]:
            visited[new_x][new_y][new_z] = True
            queue.append((new_x, new_y, new_z, cnt + 1))
                

