# 복습 - 전쟁 - 전투
# https://www.acmicpc.net/problem/1303

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(input().rstrip()))

def solution():
    visited = [[False] * (m) for _ in range(n)]
    answer = [0, 0]

    def bfs(x, y, color):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        cnt = 1
        while queue:
            curr_x, curr_y = queue.popleft()
            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    if not visited[new_x][new_y]:
                        if data[new_x][new_y] == color:
                            visited[new_x][new_y] = True
                            queue.append((new_x, new_y))
                            cnt += 1
        return cnt ** 2
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if data[i][j] == 'B':
                    answer[1] += bfs(i, j, data[i][j])
                else:
                    answer[0] += bfs(i, j, data[i][j])

    return answer

answer = solution()
print(*answer)
