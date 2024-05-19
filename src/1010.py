# 다리 놓기
# https://www.acmicpc.net/problem/1010
# 수학, 다이나믹 프로그래밍, 조합론

# =======================================
import sys
from math import comb
input = sys.stdin.readline

def solution(n, m):
    cnt = 0
    for i in range(0, m-n+1):
        cnt += comb(m-i-1, n-1)
    return cnt

    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(solution(n, m))