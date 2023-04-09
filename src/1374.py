# 강의실
# https://www.acmicpc.net/problem/1374
# 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

# =======================================
from heapq import heappush, heappop


N = int(input())

cnt = 1
heap = [] # start 값 기준으로 최소 힙 정렬
for i in range(N):
    # 강의 번호, 강의 시작 시간, 강의 종료 시간
    num, start, end = (map(int, input().split()))
    heappush(heap, [start, end, num]) # 강의 시작 시간을 기준으로 힙 생성

end_heap = [] # end 값 기준으로 최소 힙 정렬
while heap:
    # minHeap의 end 값을 따로 heap에 관리
    heappush(end_heap, heap[0][1])
    # print(f"Before heappop : start_min : {heap[0][0]} // end_min  : {end_heap[0]}")

    heappop(heap)
    
    if len(heap) == 0:
        break

    # print(f"After heappop : start_min : {heap[0][0]}")

    if heap[0][0] >= end_heap[0]:
        heappop(end_heap)
    else:
        cnt += 1

print(cnt)