# 빙산
# https://www.acmicpc.net/problem/2573
# 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# 전체 그래프
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 빙산 그래프
ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
year = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    sea_list = []
    # 빙산 주변의 바다 개수를 센 후 
    # 바다 개수만큼 녹는다. (한 해에)
    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 빙산 주변이 바다인 경우
                if graph[nx][ny] == 0:
                    sea += 1 # 바다 개수 카운트
                # 빙산 주변이 미방문 빙산인 경우
                elif not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
        # 바다 개수만큼 녹일 준비
        if sea > 0:
            sea_list.append((x, y, sea))
    # 빙산 녹이기
    for x, y, sea in sea_list:
        graph[x][y] = max(0, graph[x][y] - sea)
    
    return 1


# 빙산이 다 녹을 때까지
while ice:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    ice_to_sea = []
    group = 0
    for i, j in ice:
        # 해가 지날 때 마다 그룹 개수 세기
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        # 빙산이 바다가 된 경우 check
        if graph[i][j] == 0:
            ice_to_sea.append((i, j))

    if group > 1:
        print(year)
        exit(0)

    # 빙산 리스트 초기화 (바다가 된 빙산은 앞으로 셀 필요가 없기 때문)
    ice = sorted(list(set(ice) - set(ice_to_sea)))
    year += 1

print(0)


