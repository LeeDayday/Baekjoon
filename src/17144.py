# 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치 찾기 (첫 열에 -1이 2칸 연속)
pur = []
for i in range(r):
    if board[i][0] == -1:
        pur.append(i)
upper, lower = pur[0], pur[1]

# 먼지 확산
def spread():
    tmp = [[0] * c for _ in range(r)] # 임시 배열에 누적 후 한 번에 반영
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                dust = board[i][j] // 5
                if dust == 0:
                    continue
                cnt = 0
                # 상하좌우 확산
                for dx, dy in ((-1, 0),(1, 0),(0, -1),(0, 1)):
                    new_i, new_j = i + dx, j + dy
                    if 0 <= new_i < r and 0 <= new_j < c and board[new_i][new_j] != -1:
                        tmp[new_i][new_j] += dust
                        cnt += 1
                board[i][j] -= dust * cnt
    # 누적 반영
    for i in range(r):
        for j in range(c):
            if board[i][j] != -1:
                board[i][j] += tmp[i][j]

# 공기 청정기
def purify():
    # 상단(반시계)
    # 위쪽: 위로 올리기
    for i in range(upper - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    # 왼->오 위 행
    for j in range(0, c - 1):
        board[0][j] = board[0][j + 1]
    # 위->아래 오른쪽 열
    for i in range(0, upper):
        board[i][c - 1] = board[i + 1][c - 1]
    # 오->왼 upper 행
    for j in range(c - 1, 1, -1):
        board[upper][j] = board[upper][j - 1]
    board[upper][1] = 0  # 청정기 옆칸은 깨끗한 공기

    # 하단(시계)
    # 아래쪽: 아래로 내리기
    for i in range(lower + 1, r - 1):
        board[i][0] = board[i + 1][0]
    # 왼->오 아래 행
    for j in range(0, c - 1):
        board[r - 1][j] = board[r - 1][j + 1]
    # 아래->위 오른쪽 열
    for i in range(r - 1, lower, -1):
        board[i][c-1] = board[i - 1][c - 1]
    # 오->왼 lower 행
    for j in range(c - 1, 1, -1):
        board[lower][j] = board[lower][j - 1]
    board[lower][1] = 0  # 청정기 옆칸 초기화

# t초 동안 먼지 확산 & 공기 청정 진행
for _ in range(t):
    spread()
    purify()

# t 초 후 남은 먼지
ans = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            ans += board[i][j]
print(ans)
