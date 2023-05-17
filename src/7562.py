# 나이트의 이동
# https://www.acmicpc.net/problem/7562
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if x == goal_pos[0] and y == goal_pos[1]:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

    return board[goal_pos[0]][goal_pos[1]]

t = int(sys.stdin.readline())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

for _ in range(t):
    l = int(sys.stdin.readline())
    board = [[0 for _ in range(l)] for _ in range(l)]
    x, y = map(int, sys.stdin.readline().split())
    goal_pos = list(map(int, sys.stdin.readline().split()))
    print(bfs(x, y))

