# 스택
# https://www.acmicpc.net/problem/10828
# 자료구조, 스택

# =======================================
from collections import deque
import sys

n = int(sys.stdin.readline())
stack = deque()

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)

