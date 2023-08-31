# RGB 거리
# https://www.acmicpc.net/problem/1149
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    houses = []

    for _ in range(n):
        houses.append(list(map(int, input().split())))

    # 이전 단계 and 다른 색 and 최소비용 + 현재 비용
    for i in range(1, n):
        # i 번째 집까지의 최소 비용 구하기

        # i 번째 집이 r인 경우
        houses[i][0] = min(houses[i-1][1], houses[i-1][2]) + houses[i][0]
        # i 번째 집이 g인 경우
        houses[i][1] = min(houses[i-1][0], houses[i-1][2]) + houses[i][1]
        # i 번째 집이 b인 경우
        houses[i][2] = min(houses[i-1][0], houses[i-1][1]) + houses[i][2]

    print(min(houses[n-1]))