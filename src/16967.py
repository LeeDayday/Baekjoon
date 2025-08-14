# 배열 복원하기
# https://www.acmicpc.net/problem/16967

# 구현

import sys
input = sys.stdin.readline

# h x w 크기의 배열 A
# (h+x) x (w+y) 크기의 배열

h, w, x, y = map(int, input().split())

list_b = [list(map(int, input().split())) for _ in range(h+x)]

list_a = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        list_a[i][j] = list_b[i][j]

# 겹친 부분만 빼기
for i in range(x, h):
    for j in range(y, w):
        list_a[i][j] = list_b[i][j] - list_a[i - x][j - y]

for i in range(h):
    print(*list_a[i])