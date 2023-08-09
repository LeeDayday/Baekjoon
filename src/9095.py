# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
# 다이나믹 프로그래밍

# =======================================
from sys import stdin
input = stdin.readline

def find_cnt(num):
    if num < 4:
        return
    if dp[num-3] * dp[num-2] * dp[num-1] == 0:
       find_cnt(num-1) 
    
    dp[num] = dp[num-3] + dp[num-2] + dp[num-1]

if __name__ == '__main__':
    n = int(input())
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for _ in range(n):
        num = int(input())
        find_cnt(num)
        print(dp[num])

