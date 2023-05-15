# 최솟값 찾기
# https://www.acmicpc.net/problem/11003
# 자료구조, 우선순위 큐, 덱

# =======================================
from collections import deque
import sys

n, l = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

# deque: for문을 통해 순차적으로 arr 오름차순 (값, idx) 저장
# l의 범위를 벗어난 경우, pop
deque = deque()

for i in range(n):
    # 오름차순을 유지하기 위한 pop 작업
    while deque and deque[-1][0] > arr[i]:
        deque.pop()
    # 최솟값의 idx가 범위를 벗어난 경우, popleft
    while deque and deque[0][1] < i-l+1:
        deque.popleft()
    
    deque.append((arr[i], i))
    print(deque[0][0], end=' ')