# 복습 - 부분 문자열
# https://www.acmicpc.net/problem/16916

import sys, re
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()
def solution():
    if p in s:
        return 1
    else:
        return 0

print(solution())


