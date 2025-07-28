# 복습 - 연구소
# https://www.acmicpc.net/problem/14502

# O(N^2) x O(NM) = O(N^3M)

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 0: 빈 칸, 1: 벽, 2: 바이러스
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# bfs 수행을 시작할 바이러스 위치 찾기
virus = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            virus.append((i, j))

answer = (
    0 # 최종 정답 (안전 영역 크기의 최댓값)
)

def bfs() -> None:
    global answer
    queue = deque()
    graph = deepcopy(data)
    visited = [[False] * m for _ in range(n)]
    for x, y in virus:
        queue.append((x, y))
        visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if graph[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    queue.append((new_x, new_y))
                    graph[new_x][new_y] = 2
                    visited[new_x][new_y] = True
    
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result += 1
    answer = max(answer, result)
    return

def set_wall(cnt: int) -> None:
    if cnt == 3: # 세운 벽이 3개가 된다면 bfs 수행
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1 # 벽 세우기
                set_wall(cnt + 1)
                data[i][j] = 0 # 벽 허물기


set_wall(0)     
print(answer)       
