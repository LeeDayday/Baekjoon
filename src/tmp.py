# 복습 - 빗물
# https://www.acmicpc.net/problem/14719

# O(N)

import sys
input = sys.stdin.readline

h, w = map(int, input().split())

data = list(map(int, input().split()))

answer = 0
# 진행 방향에 대한 최대 높이 저장
left_to_right = [0] * w
right_to_left = [0] * w

left_to_right[0] = data[0]
for i in range(1, w):
    left_to_right[i] = max(left_to_right[i - 1], data[i])
right_to_left[-1] = data[-1]
for i in range(w - 2, -1, -1):
    right_to_left[i] = max(right_to_left[i + 1], data[i])

# 빗물 양 계산
for i in range(1, w - 1):
    rain = min(left_to_right[i], right_to_left[i])
    # 빗물이 반드시 고이는 경우
    if  rain > data[i]:
        answer += rain - data[i]

print(answer)