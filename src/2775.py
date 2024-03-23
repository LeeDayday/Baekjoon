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
        rooms = [[0 for _ in range(n+1)]for _ in range(k+1)] 
        # 0층의 i호엔 i명이 산다
        # 모든 층의 1호엔 1명이 산다
        for i in range(n+1):
            rooms[0][i] = i
        for i in range(k+1):
            rooms[i][1] = 1
      
        for i in range(1, k+1):
            for j in range(1, n+1):
                rooms[i][j] = rooms[i][j - 1] + rooms[i - 1][j]

        print(rooms[-1][-1])


if __name__ == '__main__':
    solution()