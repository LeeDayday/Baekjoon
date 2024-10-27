# BOJ 거리
# https://www.acmicpc.net/problem/12026
# 다이나믹 프로그래밍

# =======================================
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
data = input().rstrip()

dp = [INF] * (n)

# 시작은 무조건 1번 B
dp[0] = 0
queue = deque()
queue.append(0)

turn = ['B', 'O', 'J']
def get_next_ch(idx):
    for i in range(3):
        if data[idx] == turn[i]:
            return turn[(i + 1) % 3]
for i in range(n):
    next_ch = get_next_ch(i)
    for j in range(i + 1, n):
        if data[j] == next_ch:
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])