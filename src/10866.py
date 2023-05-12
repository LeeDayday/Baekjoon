# 덱
# https://www.acmicpc.net/problem/10866
# 자료구조, 덱

# =======================================
from collections import deque
import sys

deque = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        deque.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deque.append(cmd[1])
    elif cmd[0] == 'pop_front':
        try:
            print(deque.popleft())
        except:
            print(-1)
    elif cmd[0] == 'pop_back':
        try:
            print(deque.pop())
        except:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        if len(deque):
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        try:
            print(deque[0])
        except:
            print(-1)
    elif cmd[0] == 'back':
        try:
            print(deque[-1])
        except: 
            print(-1)
