# 줄세우기
# https://www.acmicpc.net/problem/10431
# 구현, 정렬, 시뮬레이션

# =======================================
import sys
input = sys.stdin.readline

def solution(data, n):
    cnt = 0
    for i in range(1, n):
        target = i
        while target > 0:
            if data[target - 1] > data[target]:
                data[target - 1], data[target] = data[target], data[target - 1]
                target -= 1
                cnt += 1
            else:
                break
    return cnt

for _ in range(int(input())):
    data = list(map(int, input().split()))

    print(data[0], solution(data[1:], len(data[1:])))