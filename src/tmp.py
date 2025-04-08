# 복습 - BOJ 거리
# https://www.acmicpc.net/problem/12026

# O(n^2)

import sys
input = sys.stdin.readline

n = int(input())
data = input().rstrip()

dp = [float('inf')] * n
dp[0] = 0

dx = ['B', 'O', 'J']
def get_next_ch(curr_ch):
    for i in range(3):
        if dx[i] == curr_ch:
            return dx[(i + 1) % 3]

def solution():
    if data[0] != 'B':
        return -1
    for i in range(n):
        new_ch = get_next_ch(data[i])
        for j in range(i + 1, n):
            if data[j] == new_ch:
                dp[j] = min(dp[j], dp[i] + (j - i) * (j - i)) # (j - i)칸 만큼 jump

    if dp[-1] == float('inf'):
        return -1
    return dp[-1]

print(solution())