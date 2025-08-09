# 구슬 탈출 2
# https://www.acmicpc.net/problem/13450

# 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]


rx, ry = 0, 0
bx, by = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx = i
            ry = j
        elif graph[i][j] == 'B':
            bx = i
            by = j

def bfs(rx:int, ry:int, bx:int, by:int)->int:
    answer = 0
    queue = deque()
    queue.append((rx, ry, bx, by)) # (빨간 공 위치), (파란 공 위치)
    visited = [] # 빨간 공 위치, 파란 공 위치를 함께 저장하여 두 공의 위치 동시에 파악하기
    visited.append((rx, ry, bx, by))

    while queue:
        #print(answer, queue)
        for _ in range(len(queue)):
            curr_rx, curr_ry, curr_bx, curr_by = queue.popleft()
            if answer > 10:
                return -1
            if graph[curr_rx][curr_ry] == 'O': # 빨간 구슬이 구멍에 도달한 경우
                return answer
            for i in range(4):
                # 빨간 공 이동
                new_rx = curr_rx
                new_ry = curr_ry
                while True: # 한 방향으로 이동할 수 있을 때까지 이동
                    new_rx += dx[i]
                    new_ry += dy[i]
                    if graph[new_rx][new_ry] == '#': # 벽
                        new_rx -= dx[i]
                        new_ry -= dy[i]
                        break
                    if graph[new_rx][new_ry] == 'O': # 구멍. 더 이상 해당 방향으로 이동할 필요가 없음
                        break
                # 파란 공 이동
                new_bx = curr_bx
                new_by = curr_by
                while True:
                    new_bx += dx[i]
                    new_by += dy[i]
                    if graph[new_bx][new_by] == '#': # 벽
                        new_bx -= dx[i]
                        new_by -= dy[i]
                        break
                    if graph[new_bx][new_by] == 'O': # 구멍
                        break
                if graph[new_bx][new_by] == 'O': # 파란색 공이 구멍에 도달한 경우는 제외
                    continue
                if new_rx == new_bx and new_ry == new_by: # 두 공이 충돌한 경우
                    # 먼저 해당 위치에 있던 공(=위치 변화량이 적은 공)이 기존 위치 유지
                    if abs(new_rx - curr_rx) + abs(new_ry - curr_ry) > abs(new_bx - curr_bx) + abs(new_by - curr_by):
                        new_rx -= dx[i]
                        new_ry -= dy[i]
                    else:
                        new_bx -= dx[i]
                        new_by -= dy[i]
                if (new_rx, new_ry, new_bx, new_by) not in visited:
                    queue.append((new_rx, new_ry, new_bx, new_by))
                    visited.append((new_rx, new_ry, new_bx, new_by))
        answer += 1
    return -1

print(bfs(rx, ry, bx, by))

    
