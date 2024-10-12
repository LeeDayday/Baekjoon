# 알고스팟
# https://www.acmicpc.net/problem/1261
# 그래프 이론, 그래프 탐색, 최단 경로, 데이크스트라, 0-1 너비 우선 탐색

# =======================================
import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, m, n):
    queue = deque()
    queue.append((0, 0))

    # 벽 부순 횟수 저장 (visited 동시에 관리)
    cnt = [[-1] * m for _ in range(n)]
    cnt[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                # 빈 방인 경우, 벽을 부수지 않고 이동
                if graph[new_x][new_y] == 0:
                    # [new_x][new_y] 를 방문한 적이 없거나, [new_x][new_y] 비용 update가 필요한 경우
                    if cnt[new_x][new_y] == -1 or cnt[new_x][new_y] > cnt[x][y]:
                        cnt[new_x][new_y] = cnt[x][y]
                        queue.appendleft((new_x, new_y)) # 벽을 부수지 않은 경우는 queue 앞쪽에 추가
                # 벽인 경우, 벽을 부수고 이동
                elif graph[new_x][new_y] == 1:
                    # [new_x][new_y]를 방문한 적이 없거나,  [new_x][new_y] 비용 update가 필요한 경우
                    if cnt[new_x][new_y] == -1 or cnt[new_x][new_y] > cnt[x][y] + 1:
                        cnt[new_x][new_y] = cnt[x][y] + 1
                        queue.append((new_x, new_y))
    return cnt[-1][-1]

m, n = map(int, input().split()) # 가로, 세로
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

print(bfs(graph, m, n))