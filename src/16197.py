# 두 동전전
# https://www.acmicpc.net/problem/16197
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

coins = [] # 동전 두 개의 초기 위치
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            coins.append((i, j))

def bfs():
    queue = deque()
    queue.append((coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0))  # (x1, y1, x2, y2, 버튼 누른 횟수수)
    
    while queue:
        x1, y1, x2, y2, count = queue.popleft()

        # 10번 초과 시 실패
        if count >= 10:
            return -1

        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]

            # 동전 1과 동전 2가 떨어졌는지 체크
            out1 = not (0 <= nx1 < n and 0 <= ny1 < m)  # 동전 1이 떨어졌는지
            out2 = not (0 <= nx2 < n and 0 <= ny2 < m)  # 동전 2가 떨어졌는지
            
            # 하나만 떨어진 경우 정답
            if out1 ^ out2:
                return count + 1
            
            # 둘 다 떨어지면 안 됨
            if out1 and out2:
                continue
            
            # 벽이면 이동하지 않음
            if 0 <= nx1 < n and 0 <= ny1 < m and graph[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if 0 <= nx2 < n and 0 <= ny2 < m and graph[nx2][ny2] == '#':
                nx2, ny2 = x2, y2
            
            queue.append((nx1, ny1, nx2, ny2, count + 1))

    return -1  # 가능한 경우가 없을 때

print(bfs())
