# 복습 - 사탕 게임
# https://www.acmicpc.net/problem/3085

import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(input().rstrip()))

# 먹을 수 있는 사탕의 최대 개수 반환
def count_max_candy():
    cnt_row = 1 # 각 행에서의 사탕 최대 개수
    # 행 검사
    for i in range(n):
        start, end = 0, 0
        while end < n:
            if data[i][start] == data[i][end]:
                end += 1
            else:
                cnt_row = max(cnt_row, end - start)
                start = end
        cnt_row = max(cnt_row, end - start)
    # 열 검사
    cnt_col = 1 # 각 열에서의 사탕 최대 개수
    for i in range(n):
        start, end = 0, 0
        while end < n:
            if data[start][i] == data[end][i]:
                end += 1
            else:
                cnt_col = max(cnt_col, end - start)
                start = end
        cnt_col = max(cnt_col, end - start)
    return max(cnt_row, cnt_col)


def solution():
    answer = 0
    dx = [1, 0]
    dy = [0, 1]

    for x in range(n):
        for y in range(n):
            for i in range(2):
                # 인접한 칸의 위치
                next_x = x + dx[i]
                next_y = y + dy[i]

                if next_x < n and next_y < n:                 
                    # 인접한 두 칸의 색이 다른 경우
                    if data[x][y] != data[next_x][next_y]:
                        # swap
                        data[x][y], data[next_x][next_y] = data[next_x][next_y], data[x][y]
                        # 먹을 수 있는 사탕 개수 계산
                        answer = max(answer, count_max_candy())
                        # 사탕 다시 원위치
                        data[x][y], data[next_x][next_y] = data[next_x][next_y], data[x][y]            

    return answer
    
print(solution())
