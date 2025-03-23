# 복습 - 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
data = []

for _ in range(n):
    data.append(list(input().rstrip()))

def solution():
    answer = []
    def bfs(data, x, y):
        queue = deque()
        queue.append((x, y))
        data[x][y] = '0' # 방문 처리
        result = 1 # 단지 수
        while queue:
            curr_x, curr_y = queue.popleft()
            for i in range(4):
                new_x = curr_x + dx[i]
                new_y = curr_y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < n:
                    if data[new_x][new_y] == '1':
                        queue.append((new_x, new_y))
                        data[new_x][new_y] = '0'
                        result += 1

        return result
                        
    for i in range(n):
        for j in range(n):
            if data[i][j] == '1':
                answer.append(bfs(data, i, j))
    
    answer.sort()
    return answer

answer = solution()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
