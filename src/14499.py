# 주사위 굴리기
# https://www.acmicpc.net/problem/14499
# 구현, 시뮬레이션

# =======================================
import sys
input = sys.stdin.readline

dx = [1, 0, 0, -1] # idx 별로 남, 동, 서, 북
dy = [0, 1, -1, 0]
# 지도 크기: n x m
# 주사위를 놓은 곳의 좌표: (x, y)
# k: 명령의 개수
n, m, x, y, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

def roll_dice(pos:int, dice:list[int]) -> None:
    # 주사위를 pos 방향으로 굴리기

    if pos == 1: # 동쪽으로 굴린 경우
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]
    elif pos == 2: # 서쪽으로 굴린 경우
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]
    elif pos == 3: # 북쪽으로 굴린 경우
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]
    elif pos == 4: # 남쪽으로 굴린 경우
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]

dice = [0, 0, 0, 0, 0, 0] # 윗면, 아랫면, 앞면, 뒷면, 오른쪽 면, 왼쪽 면


for cmd in commands:
    new_x = x + dx[cmd % 4]
    new_y = y + dy[cmd % 4]
    if 0 <= new_x < n and 0 <= new_y < m:

        roll_dice(cmd, dice)
        if data[new_x][new_y] == 0:
            data[new_x][new_y] = dice[1] # 칸 <- 주사위 바닥면
        else:
            dice[1] = data[new_x][new_y] # 주사위 바닥면 <- 칸
            data[new_x][new_y] = 0 # 칸 <- 0
        print(dice[0]) # 이동할 때마다 주사위 윗면 출력
        x = new_x
        y = new_y