# 마라톤 1
# https://www.acmicpc.net/problem/10655

# 구현, 브루트포스 알고리즘, 기하학

import sys
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 원래 총 거리
total = 0
for i in range(1, n):
    total += manhattan(data[i-1], data[i])

# 한 점 생략 시 절약되는 최대 거리
best_saved = 0
for i in range(1, n-1):  # 1..n-2 (0-index 기준)
    saved = manhattan(data[i-1], data[i]) + manhattan(data[i], data[i+1]) - manhattan(data[i-1], data[i+1])
    if saved > best_saved:
        best_saved = saved

print(total - best_saved)
