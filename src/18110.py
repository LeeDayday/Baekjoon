# solved.ac
# https://www.acmicpc.net/problem/18110
# 수학, 구현, 정렬

# =======================================
import sys
input = sys.stdin.readline


def round_traditional(num):
    return int(num+0.5)
    
n = int(input())

level = []
for _ in range(n):
    level.append(int(input()))

level.sort()

l = round_traditional(n * 0.15)
r = n - l

if n > 0:
    print(round_traditional(sum(level[l:r])/(n-2*l)))
else:
    print(0)