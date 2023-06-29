# 로봇 청소기
# https://www.acmicpc.net/problem/14503
# 구현, 시뮬레이션

# =======================================
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

x, y, d = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 북, 동, 남, 서 (시계)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def run(x, y, d):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = -1
    cnt = 1

    while queue:
        # 현재 칸
        x, y = queue.popleft()

        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다
        if graph[x][y] == 0:
            graph[x][y] = -1
            cnt += 1

        # 주변 4칸 중 청소되지 않은 빈 칸 찾기
        flag = 0
        for i in range(4):
            # 반시계 방향으로 회전
            d = (d+3) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            # 빈 칸이 있는 경우 한 칸 전진
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    flag = 1
                    break
        # 빈 칸이 있는 경우 1번으로 돌아간다       
        if flag == 1:
            continue
        # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        nx = x - dx[d]
        ny = y - dy[d]
        # 후진할 수 없는 경우
        if graph[nx][ny] == 1:
            return cnt
        else:
            queue.append((nx, ny))

    return cnt

print(run(x, y, d))

