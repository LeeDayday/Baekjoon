# Divisors Again
# https://www.acmicpc.net/problem/13226
# 수학, 정수론

# =======================================
import sys
input = sys.stdin.readline

data = [0] * (10000001)

for i in range(1, 10000001):
    for j in range(i, 10000001, i):
        data[j] += 1

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(max(data[l:r+1]))
