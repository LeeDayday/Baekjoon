# 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847
# 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

data = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-2, -1, -1):
    if data[i] >= data[i+1]:
        cnt += data[i] - data[i+1] + 1
        data[i] = data[i+1] - 1

print(cnt)