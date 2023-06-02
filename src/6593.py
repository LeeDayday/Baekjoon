# 상범 빌딩
# https://www.acmicpc.net/problem/6593
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

da = [-1, 1, 0, 0, 0, 0]
db = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))
    graph[a][b][c] = 0 # 방문 처리

    while queue:
        a, b, c = queue.popleft()
        for i in range(6):
            na = a + da[i]
            nb = b + db[i]
            nc = c + dc[i]

            if na < 0 or nb < 0 or nc < 0 or na >=L or nb >=R or nc >= C:
                continue

            if graph[na][nb][nc] == 'E':
                return graph[a][b][c] + 1
            
            if graph[na][nb][nc] == '.':
                graph[na][nb][nc] = graph[a][b][c] + 1 # 방문 처리
                queue.append((na, nb, nc))
    return 0

def find_S():
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    return i, j, k

while True:
    L, R, C = map(int, sys.stdin.readline().split())

    if L*R*C == 0:
        break

    graph = []

    for i in range(L):
        row = []
        for j in range(R):
            row.append(list(sys.stdin.readline().rstrip()))
        input() # 빈 줄 입력받기
        graph.append(row)

    i, j, k = find_S()

    cnt = bfs(i, j, k)

    if cnt:
        print(f"Escaped in {cnt} minute(s).")
    else:
        print("Trapped!")
