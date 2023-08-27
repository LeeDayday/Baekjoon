# 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

def bfs(idx):
    queue = deque()
    queue.append(idx)
    # 방문 처리
    visited[idx] = True
    while queue:
        idx = queue.popleft()
        # 주사위 1회에 100번 칸에 도달할 수 있는 경우
        if idx == 100:
            print(graph[100])
        
        for num in range(1, 7):
            n_idx = idx + num
            # 범위를 벗어난 경우 반복문 종료
            if n_idx > 100:
                break
            # 미방문 영역인 경우
            if visited[n_idx] is False:
                # 이동할 위치에 사다라기 있는 경우
                if n_idx in ladders.keys():
                    # 사다리의 종착점으로 이동
                    n_idx = ladders[n_idx]
                # 이동할 위치에 뱀이 있는 경우
                if n_idx in snakes.keys():
                    # 뱀의 종착점으로 이동
                    n_idx = snakes[n_idx]
                # 사다리/ 뱀 이후의 최종 종착점이 미방문 영역인 경우
                if visited[n_idx] is False:
                    # 방문 표시
                    visited[n_idx] = True
                    graph[n_idx] = graph[idx] + 1
                    queue.append(n_idx)

                


n, m = map(int, input().split())

# 전체 게임판
graph = [0 for _ in range(101)] # idx 1부터 유의미한 값 
# 방문 여부
visited = [False for _ in range(101)] # idx 1부터 유의미한 값
# 사다리 정보
ladders = {}
for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

# 뱀 정보
snakes = {}
for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v

bfs(1)
