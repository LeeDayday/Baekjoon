# 회전하는 큐
# https://www.acmicpc.net/problem/1021
# 자료구조, 덱

# =======================================
from collections import deque
import sys
    
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

queue = deque()
cnt = 0

for i in range(n):
    queue.append(i+1)

for num in arr:
   
    while True:
        idx = queue.index(num)

        if idx == 0:
            queue.popleft()
            break

        if idx > len(queue) // 2:
            queue.appendleft(queue.pop())
        else:
            queue.append(queue.popleft())
        cnt += 1

print(cnt)
    