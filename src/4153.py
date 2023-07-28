# 직각삼각형
# https://www.acmicpc.net/problem/4153
# 수학, 기하학, 피타고라스 정리

# =======================================
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    while True:
        a, b, c = map(int, input().split())
        if a + b + c == 0:
            exit()
        s_a, s_b, s_c = a ** 2, b ** 2, c ** 2
        # 세 변의 제곱 길이 합 == 빗변의 제곱 길이 * 2 이면 직각 삼각형
        if s_a + s_b + s_c == max(s_a, s_b, s_c) * 2:
            print("right")
        else:
            print("wrong")
