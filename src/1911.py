# 흙길 보수하기
# https://www.acmicpc.net/problem/1911
# 정렬, 스위핑
# =======================================
import sys
from math import ceil

n, l = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()

start, end = 0, 0 # 널빤지 시작점, 끝
cnt = 0
for i in range(n):
    # 널빤지 시작점

    if end >= arr[i][0]: # 웅덩이에 널빤지가 이미 있는 경우
        start = end + 1
    else:
        start = arr[i][0]
    # 웅덩이 길이
    distance = arr[i][1] - start

    # 필요한 널빤지 개수
    wood = ceil(distance / l)

    # 널빤지 끝점
    end = start + wood * l - 1
    print(f"start:{start}, end:{end}, dis:{distance}, wood:{wood}")
    # 총 널빤지 개수
    cnt += wood

print(wood)