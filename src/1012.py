# 유기농 배추
# https://www.acmicpc.net/problem/1012
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
from collections import deque
import sys
sys.setrecursionlimit(10000)

def DFS(x, y):
    # 범위를 벗어난 경우
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    # 배추가 있는 경우
    if graph[y][x] == 1:
        # 해당 배추밭 방문 처리
        graph[y][x] = 0
        # 상, 하, 좌, 우 접근
        DFS(x, y-1)
        DFS(x, y+1)
        DFS(x-1, y)
        DFS(x+1, y)
        return True
    # 배추가 없는 경우
    return False


t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if DFS(j, i) is True:
                cnt += 1
    
    print(cnt)