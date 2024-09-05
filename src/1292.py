# 쉽게 푸는 문제
# https://www.acmicpc.net/problem/1292
# 수학, 구현

# =======================================
import sys
input = sys.stdin.readline


data = [0]
for i in range(46):
    for j in range(i):
        data.append(i)

a, b = map(int, input().split())
print(sum(data[a:b+1]))