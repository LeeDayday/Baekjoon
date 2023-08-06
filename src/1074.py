# Z
# https://www.acmicpc.net/problem/1074
# 분할 정복 재귀

# =======================================
import sys
input = sys.stdin.readline

# Z 모양 이동 방향
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

# 방문 횟수
cnt = 0

# 사분면 기준
# 1사분면 2사분면
# 3사분면 4사분면 
def find_quadrant(n, r, c):

    half_len = 2 ** (n-1)

    if r < half_len:
        if c < half_len:
            return 1
        else:
            return 2
    else:
        if c < half_len:
            return 3
        else:
            return 4
        
def search_z(n, goal_x, goal_y):
    global cnt # 전역변수 선언
    # basecase: 4칸짜리 z만 탐색하면 되는 경우
    if n == 1:
        for i in range(4):
            if dx[i] == goal_x and dy[i] == goal_y:
                return
            cnt += 1
    # 목표 좌표가 어느 사분면에 속하는지 구하기
    quad = find_quadrant(n, goal_x, goal_y)
    # 지나온 사분면 cnt 값 계산
    cnt += (quad-1)*((2**(n-1))**2)
    # 1사분면으로 범위 좁히기
    search_z(n-1, goal_x % (2 ** (n-1)), goal_y % (2 ** (n-1)))

n, r, c = map(int, input().split())

search_z(n, r, c)
print(cnt)