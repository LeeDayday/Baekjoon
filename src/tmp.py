# 복습 - 로봇 청소기
# https://www.acmicpc.net/problem/14503

# O(NM)

import sys
input = sys.stdin.readline

# index 별로 북, 동, 남, 서를 가리킴
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

n, m = map(int, input().split()) # 방의 크기
r, c, d = map(int, input().split()) # (r, c): 로봇 청소기 초기 좌표, d: 로봇 청소기 초기 방향

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


answer = 0
while True:
    if data[r][c] == 0:
        data[r][c] = 2  # 청소
        answer += 1

    cleaned = False
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향 회전
        nx = r + dx[d]
        ny = c + dy[d]
        # 청소되지 않은 빈칸이 있는 경우 전진
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
            r, c = nx, ny
            cleaned = True
            break

    if not cleaned:
        # 후진
        back = (d + 2) % 4
        nx = r + dx[back]
        ny = c + dy[back]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 1:
            r, c = nx, ny
        else:
            break

print(answer)