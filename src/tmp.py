# 복습 - 미로탐색
# https://www.acmicpc.net/problem/2178

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().rstrip())))

# 최단 거리 & 도착 보장 -> bfs
def bfs():
    visited = [[False] * (m) for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        curr_x, curr_y = queue.popleft()
        if curr_x == n - 1 and curr_y == m - 1:
            break
        for i in range(4):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if not visited[new_x][new_y] and data[new_x][new_y] == 1:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
                    data[new_x][new_y] = data[curr_x][curr_y] + 1
    
    return data[-1][-1]
    

print(bfs())