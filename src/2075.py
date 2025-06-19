# N번째 큰 수
# https://www.acmicpc.net/problem/2075
# 

# =======================================
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    for num in map(int, input().split()):
        heappush(heap, num)

        if len(heap) > n:
            heappop(heap)
        print(f"heap:{heap}")
print(heap)
print(heappop(heap))

