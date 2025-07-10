# 복습 - 인구 이동
# https://www.acmicpc.net/problem/16234

# 


import sys
from collections import deque
input = sys.stdin.readline

# n x n 크기의 땅
# 국경선을 공유하는 두 나라의 인구 차이가 [l, r]이면, 국경선 open, 인구 이동 시작
# 인구 이동 시, 각 칸의 이동 수는 (연합의 인구 수) / (연합 개수)
# 국경선 close
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, l, r = map(int, input().split()) 

def bfs(data, team, i, j, num):
    queue = deque()
    queue.append((i, j))

    indexes = [(i, j)]
    sum_ = data[i][j]
    total = 1
    team[i][j] = num
    
    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue
            if team[new_x][new_y] == -1 and l <= abs(data[curr_x][curr_y] - data[new_x][new_y]) <= r:
                queue.append((new_x, new_y))
                team[new_x][new_y] = num
                indexes.append((new_x, new_y))
                sum_ += data[new_x][new_y]
                total += 1
    
    for i, j in indexes:
        data[i][j] = sum_ // total

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

answer = 0

while True:
    team = [[-1] * n for _ in range(n)] # 연합 발생 여부 및 순서
    num = 0
    for i in range(n):
        for j in range(n):
            if team[i][j] == -1:
                # 연합의 크기가 2칸 이상이어야 인구 이동으로 인정
                bfs(data, team, i, j, num)
                num += 1
    if num == n * n: # 아무 인구 이동 발생 없이 모든 칸을 돈 경우, 더 이상 인구 이동을 할 수 없다는 뜻
        break
    answer += 1

print(answer)