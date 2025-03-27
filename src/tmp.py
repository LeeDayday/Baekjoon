# 복습 - A -> B
# https://www.acmicpc.net/problem/16953

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1
while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        break
    cnt += 1

print(cnt if b == a else -1)
