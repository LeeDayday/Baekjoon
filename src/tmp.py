# 복습 - 음식물 피하기
# https://www.acmicpc.net/problem/1743

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m, k = map(int, input().split())

data = [[0] * (m) for _ in range(n)]
positions = set()
for _ in range(k):
    r, c = map(int, input().split())
    positions.add((r - 1, c - 1))
    data[r - 1][c - 1] = 1

def solution():
    answer = 0
    visited = [[False] * (m) for _ in range(n)]
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        result = 1
        while queue:
            curr_x, curr_y = queue.popleft()
            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    if not visited[new_x][new_y] and data[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True
                        result += 1
                    
        return result
    
    for x, y in positions:
        if not visited[x][y]:
            answer = max(answer, bfs(x, y))

    return answer

print(solution())