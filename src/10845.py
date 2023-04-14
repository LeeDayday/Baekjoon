# 큐
# https://www.acmicpc.net/problem/10845
# 자료구조, 큐

# =======================================
import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
        queue.append(cmd[1])

    elif cmd[0] == 'pop':
        try:
            print(queue.pop(0))
        except:
            print(-1)

    elif cmd[0] == 'size':
        print(len(queue))

    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)

    elif cmd[0] == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)