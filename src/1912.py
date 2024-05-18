# 연속합
# https://www.acmicpc.net/problem/1912
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

def solution(n, data):
    for i in range(1, n):
        data[i] = max(data[i], data[i-1]+data[i])
    return max(data)


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    print(solution(n, data))