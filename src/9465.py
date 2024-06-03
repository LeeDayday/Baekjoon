# 스티커
# https://www.acmicpc.net/problem/9465
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        data = []
        for i in range(2):
            data.append(list(map(int, input().split())))

        dp = [[0 for _ in range(n)] for _ in range(2)]
        # 스티커 길이가 1인 경우
        dp[0][0] = data[0][0]
        dp[1][0] = data[1][0]

        if n == 1:
            print(max(dp[0][0], dp[1][0]))
            continue
        # 스티커 길이가 2인 경우
        dp[0][1] = data[0][0] + data[1][1] 
        dp[1][1] = data[1][0] + data[0][1]
        if n == 2:
            print(max(dp[0][0], dp[1][0]))
            continue
        
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + data[0][i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + data[1][i]

        print(max(dp[0][-1], dp[1][-1]))



