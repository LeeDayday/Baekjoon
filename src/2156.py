# 포도주 시식
# https://www.acmicpc.net/problem/2156
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline


def solution(n, data):
    if n == 1:
        return data[0]
    elif n == 2:
        return data[0] + data[1]
    elif n == 3:
        return max(data[0]+data[2], data[1]+data[2], data[0]+data[1])
    
    dp = [0] * n
    dp[0] = data[0]
    dp[1] = data[0] + data[1]
    dp[2] = max(data[0]+data[2], data[1]+data[2], data[0]+data[1])
    for i in range(3, n):
        dp[i] = max(dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i], dp[i-1])

    return max(dp)


if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        data.append(int(input()))
    print(solution(n, data))
    

