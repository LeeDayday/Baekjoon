# 복습 - A와 B
# https://www.acmicpc.net/problem/12904

# O(N) (N: 문자열 t의 길이)

import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip()
t = deque(input().rstrip())
reversed_flag = False
answer = 0

# t -> s
# 문자열 맨 뒤 A 삭제
# 문자열 맨 뒤 B 삭제 후 뒤집기
while len(t) >= len(s):
    if len(t) == len(s):
        if not reversed_flag:
            if ''.join(t) == s:
                answer = 1
                break
        else:
            if ''.join(reversed(t)) == s:
                answer = 1
                break    
    if not reversed_flag:
        tmp = t.pop()
    else:
        tmp = t.popleft()

    if tmp == 'B':
        reversed_flag = not reversed_flag


print(answer)
