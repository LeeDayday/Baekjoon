# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

def solution(n, data):
    dp = [1] * n 
    for i in range(1, n):
        for j in range(i):
            if data[j] < data[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return (max(dp))


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    print(solution(n, data))