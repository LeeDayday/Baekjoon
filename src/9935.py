# 문자열 폭발
# https://www.acmicpc.net/problem/9935
# 자료 구조, 문자열, 스택

# =======================================
import sys
input = sys.stdin.readline

data = input().rstrip()
pattern = input().rstrip()
p = len(pattern)

stack = []

for i in range(len(data)):
    stack.append(data[i])
    if ''.join(stack[-p:]) == pattern:
        for _ in range(p):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))