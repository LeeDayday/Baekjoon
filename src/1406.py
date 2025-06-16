# 에디터
# https://www.acmicpc.net/problem/1406
# 자료 구조, 스택, 연결 리스트

# =======================================
import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
stack2 = []

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif cmd[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif cmd[0] == 'B':
        if stack1:
            stack1.pop()
    elif cmd[0] == 'P':
        stack1.append(cmd[1])

stack1.extend(reversed(stack2))
print(''.join(stack1))