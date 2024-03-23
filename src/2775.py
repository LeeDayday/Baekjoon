# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
# 수학, 구현, 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline


def solution():
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())
        # 이차원 리스트를 선언하지 않고, 1차원 리스트 값을 계속 업데이트 하는 방법
        # 0층의 i호엔 i명이 산다 
        rooms = [i for i in range(1, n + 1)] 
        # 1층 1호부터 k층의 n호까지 값 갱신
        for i in range(k):
            for j in range(1, n):
                rooms[j] += rooms[j-1]

        print(rooms[-1])


if __name__ == '__main__':
    solution()