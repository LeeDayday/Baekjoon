# 피보나치 함수
# https://www.acmicpc.net/problem/1003
# 

# =======================================
import sys
input = sys.stdin.readline

def get_cnt(dp, n):
    if n <= 1:
        return dp[n]
    if dp[n-1] == 0:
        dp[n-1] = get_cnt(dp, n-1)
    return (dp[n-1][0]+dp[n-2][0], dp[n-1][1] + dp[n-2][1])

def solution():
    t = int(input())
    dp = [0] * (41)
    dp[0] = (1, 0)
    dp[1] = (0, 1)
    
    for _ in range(t):
        n = int(input())
        print(*get_cnt(dp, n))

    
if __name__ == '__main__':
    solution()

