# ACM 호텔
# https://www.acmicpc.net/problem/10250
# 수학, 구현, 사칙연산

# =======================================
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        h, w, n = map(int, input().split())
        floor = n % h
        room = n // h + 1    
        if floor == 0:
            floor = h
            room -= 1
        print(floor*100 + room)
