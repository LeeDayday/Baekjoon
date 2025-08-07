# 복습 - 뱀
# https://www.acmicpc.net/problem/3190

# O(T)

import sys
from collections import deque
input = sys.stdin.readline

# 동, 남, 서, 북 (시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
graph = [[0] * n for _ in range(n)] # 0: 빈 칸, 1: 사과, 2: 뱀
graph[0][0] = 2

snakes = deque()
snakes.append((0, 0)) # front: 뱀의 머리, rear: 뱀의 꼬리
idx = 0 # 뱀의 머리 방향

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

commands = deque() # 뱀의 방향 변환 정보
for _ in range(int(input())):
    commands.append(list(input().split())) # 시간, 회전 방향

for time in range(1, 10001):
    # 종료 조건: 벽 또는 자기 자신과 부딪히는 경우
    #print(f"{time}초, {snakes}")
    # 직진
    new_x = snakes[-1][0] + dx[idx]
    new_y = snakes[-1][1] + dy[idx]

    # 종료 조건: 벽 또는 자기 자신과 부딪히는 경우
    if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
        break
    if graph[new_x][new_y] == 2:
        break
    # 머리를 다음 칸에 위치시키기
    snakes.append((new_x, new_y))
    # 사과가 없는 경우
    if graph[new_x][new_y] == 0:
        # 꼬리칸 비우기
        tail_x, tail_y = snakes.popleft()
        graph[tail_x][tail_y] = 0
    # 머리 칸 방문 처리
    graph[new_x][new_y] = 2

    # 방향 변경
    if commands and commands[0][0] == str(time):
        #print(commands[0])
        if commands[0][1] == 'L':
            idx = (idx - 1) % 4
        else:
            idx = (idx + 1) % 4
        commands.popleft()

print(time)