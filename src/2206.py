# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, n, m):
    # visited[x][y][0]: 벽을 부수지 않고 방문, visited[x][y][1]: 벽을 부순 적이 있음
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 0)]) # x, y, 벽 부순 여부
    visited[0][0][0] = 1
    while queue:
        x, y, broken = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][broken]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                continue
            # 벽을 부수지 않고 이동하는 경우
            if graph[new_x][new_y] == 0 and visited[new_x][new_y][broken] == 0:
                visited[new_x][new_y][broken] = visited[x][y][broken] + 1
                queue.append((new_x, new_y, broken))
            # 벽이 있고, 벽을 부술 수 있는 경우 (벽을 부술 수 있는 기회는 한 번)
            if graph[new_x][new_y] == 1 and broken == 0:
                visited[new_x][new_y][1] = visited[x][y][broken] + 1
                queue.append((new_x, new_y, 1))

    return -1


        
def solution():
    n, m = map(int, input().split())
    graph = [list(map(int, input().rstrip())) for _ in range(n)]

    result = bfs(graph, n, m)
    print(result)

if __name__ == '__main__':
    solution()
