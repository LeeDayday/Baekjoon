# 복습 - 공유기 설치
# https://www.acmicpc.net/problem/2110

# (정렬: O(NlogN)) + (이분탐색 O(NlogD) ,D: max_dist)

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort() # 이분탐색 진행을 위한 정렬 수행

min_dist = 1
max_dist = data[-1] - data[0]

# 가장 인접한 두 공유기 사이의 최대 거리
# 어떠한 조건을 만족하도록 하는 어떤 값을 최대화
    # 직접 계산하는 방법 대신, 특정 값이 조건을 만족하는 지 판단 ... 특정값 늘려가며 판단
answer = 0
while min_dist <= max_dist:
    mid_dist = (min_dist + max_dist) // 2

    cnt = 1 # 설치한 공유기 수 (초기: data[0] 위치에 공유기 설치)
    last_pos = data[0] # 마지막으로 설치한 공유기 위치
    for i in range(1, n): # mid_dist 거리 만큼 공유기 설치
        if data[i] >= last_pos + mid_dist:
            last_pos = data[i]
            cnt += 1
    if cnt >= c: # 조건을 만족하는 경우, 거리 늘리기
        min_dist = mid_dist + 1
        answer = mid_dist
    else:
        max_dist = mid_dist - 1 # 조건을 만족하지 않는 경우, 거리 줄이기

print(answer)


