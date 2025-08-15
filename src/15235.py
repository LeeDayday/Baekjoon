# Olympiad Pizza
# https://www.acmicpc.net/problem/15235

# 구현, 자료 구조, 시뮬레이션, 큐

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

queue = deque()
answer = [0] * n

for idx, value in enumerate(data):
    queue.append((idx, value))

time = 1
while queue:
    idx, value = queue.popleft()
    if value - 1 == 0:
        answer[idx] = time
    else:
        queue.append((idx, value - 1))
    time += 1
print(*answer)