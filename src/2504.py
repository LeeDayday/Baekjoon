# 괄호의 값
# https://www.acmicpc.net/problem/2504
# 구현, 자료 구조, 스택

# =======================================
import sys
input = sys.stdin.readline

data = input().rstrip()
stack = []

total = 0
tmp = 1
for i in range(len(data)):
    if data[i] == '(' or data[i] == '[':
        stack.append(data[i])
        if data[i] == '(':
            tmp *= 2
        else:
            tmp *= 3
    else:
        # 알맞은 괄호열이 아닌 경우
        if len(stack) == 0 or (data[i] == ')' and stack[-1] == '[') or (data[i] == ']' and stack[-1] == '('):
            total = 0
            break
        mark = stack.pop()
        if data[i-1] == '(' or data[i-1] == '[':
            total += tmp
        if mark == '(':
            tmp //= 2
        elif mark == '[':
            tmp //= 3

# 알맞은 괄호열이 아닌 경우
if len(stack) != 0:
    total = 0     

print(total)
        
    