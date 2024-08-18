# 인구 이동
# https://www.acmicpc.net/problem/16234
# 구현, 그래프 이론 ,그래프 탐색, 시뮬레이션, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, l, r = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 좌표 (i, j) 기준 연합 국가 찾기
def bfs(visited, i, j, idx):
    queue = deque()
    queue.append((i, j))
    result = [] # 연결된 나라의 좌표 저장
    result.append((i, j))

    visited[i][j] = idx # 연합 번호 할당
    people_cnt = graph[i][j] # 연합 국가 총 인원 수
    cnt = 1 # 연합 국가 수
    while queue:
        curr_i, curr_j = queue.popleft()
        # 상, 하, 좌, 우 값 비교
        for i in range(4):
            new_i = curr_i + dx[i]
            new_j = curr_j + dy[i]
            if new_i < 0 or new_j < 0 or new_i >= n or new_j >= n:
                continue
            if l <= abs(graph[curr_i][curr_j] - graph[new_i][new_j]) <= r and visited[new_i][new_j] == -1:
                result.append((new_i, new_j))
                queue.append((new_i, new_j))
                visited[new_i][new_j] = idx
                people_cnt += graph[new_i][new_j]
                cnt += 1
    # 인구 이동
    moved_people = people_cnt // cnt
    for i, j in result:
        graph[i][j] = moved_people
    

# 더 이상 인구 이동을 할 수 없을 때 까지 반복
total_cnt = 0
while True:
    visited = [[-1 for _ in range(n)] for _ in range(n)] # 연합 번호 관리
    idx = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(visited, i, j, idx)
                idx += 1

    if idx == n * n: # 더 이상 인구 이동을 할 수 없는 경우
        break
    total_cnt += 1

print(total_cnt)