# 등수 구하기
# https://www.acmicpc.net/problem/1205
# 구현

# =======================================
import sys
input = sys.stdin.readline

n, target, p = map(int, input().split())

if n == 0:
    print(1)
else:
    data = list(map(int, input().split()))
    data.append(target)
    data.sort(reverse=True)

    rank = data.index(target) + 1

    if rank > p or (n == p and data[-1] == target):
        print(-1)
    else:
        print(rank)
