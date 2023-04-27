# 회의실 배정
# https://www.acmicpc.net/problem/1931
# 그리디 알고리즘, 정렬

# =======================================
import sys
from collections import deque

n = int(sys.stdin.readline())

schedules = []
for i in range(n):
    schedules.append(list(map(int, sys.stdin.readline().split())))

    
schedules.sort(key=lambda x:(x[1], x[0])) # end 기준 오름차순 정렬 -> start 기준 오름차순 정렬

cnt = 1
end_time = schedules[0][1]

for i in range(1, n):
    # print(f"-[{i}]-", end_time, schedules[i][0], cnt)
    if end_time <= schedules[i][0]:
        cnt += 1
        end_time = schedules[i][1]


print(cnt)
