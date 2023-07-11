# 강의실 배정
# https://www.acmicpc.net/problem/11000
# 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

# =======================================
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def assign_room(schedule, n):
    # 시작 시간을 기준으로 정렬
    schedule.sort()
    # 강의 종료 시간을 기준으로 min heap 형성
    heapq = []
    heappush(heapq, schedule[0][1])

    for i in range(1, n):
        curr_start = schedule[i][0]
        if heapq[0] <= curr_start:
            heappop(heapq)
        heappush(heapq, schedule[i][1])
    return len(heapq)


if __name__ == '__main__':
    n = int(input())
    schedule = []

    for _ in range(n):
        schedule.append(list(map(int, input().split())))
    
    print(assign_room(schedule, n))