# 복습 - 감시 피하기
# https://www.acmicpc.net/problem/18428

# O(eC3 * tn) => O(n^9) (e: empty 길이, t: 선생님 길이. n <= 6 이므로 시간 내 연산 가능)

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]

students = []
teachers = []
empty = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            students.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))
        else:
            empty.append((i, j))

def check_teacher() -> bool:
    # 선생님의 감시에서 벗어날 수 있는 경우 True
    for t_x, t_y in teachers:
        for i in range(4):
            new_x = t_x
            new_y = t_y
            while True:
                new_x += dx[i]
                new_y += dy[i]
                if 0 <= new_x < n and 0 <= new_y < n:
                    if graph[new_x][new_y] == 'O':
                        break
                    if graph[new_x][new_y] == 'S': # 학생이 보이면 False
                        return False
                else:
                    break
    return True
    

for comb in combinations(empty, 3):
    for x, y in comb:
        graph[x][y] = 'O'
    if check_teacher():
        print("YES")
        exit(0)
    for x, y in comb:
        graph[x][y] = 'X'
print("NO")