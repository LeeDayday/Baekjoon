# 이모티콘
# https://www.acmicpc.net/problem/14226
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[-1 for _ in range(n + 1)] for _ in range(n + 1)] # (s, c) 일 때 최소 시간

# 초기값 설정
graph[1][0] = 0
queue = deque()
queue.append((1, 0)) # (s, c)

while queue:
    s, c = queue.popleft()

    # 방법 1: 화면에 있는 이모티콘 모두 복사해서 클립보드에 저장
    if graph[s][s] == -1:
        graph[s][s] = graph[s][c] + 1
        queue.append((s, s))
    # 방법 2: 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
    if s + c <= n and graph[s + c][c] == -1:
        graph[s + c][c] = graph[s][c] + 1
        queue.append((s + c, c))
    # 방법 3: 화면에 있는 이모티콘 중 하나를 삭제
    if s - 1 >= 0 and graph[s - 1][c] == -1:
        graph[s - 1][c] = graph[s][c] + 1
        queue.append((s - 1, c))

result = int(1e9)
for c in range(n + 1):
    if graph[n][c] != -1:
        result = min(result, graph[n][c])

print(result)