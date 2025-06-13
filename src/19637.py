# IF문 좀 대신 써줘
# https://www.acmicpc.net/problem/19637
# 이분 탐색

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    name, power = input().split()
    if data and data[-1][1] == power:
        continue
    data.append([name, int(power)])


for _ in range(m):
    strength = int(input())
    start, end = 0, len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid][1] < strength:
            start = mid + 1
        else:
            end = mid - 1

    print(data[end + 1][0])