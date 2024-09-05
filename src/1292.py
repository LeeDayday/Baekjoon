# 쉽게 푸는 문제
# https://www.acmicpc.net/problem/1292
# 수학, 구현

# =======================================
import sys
input = sys.stdin.readline


data = []
num = 1
while len(data) <= 1000:
    for i in range(num):
        data.append(num)
    num += 1

a, b = map(int, input().split())
print(sum(data[a-1:b]))

