# 복습 - 문자열 폭발
# https://www.acmicpc.net/problem/9935

# O(N x M) (N: data 길이, M: target 길이)

import sys
input = sys.stdin.readline

data = input().rstrip()
target = input().rstrip()
m = len(target)
answer = []

for ch in data:
    answer.append(ch)
    if len(answer) >= m:
        if answer[-m:] == list(target):
            for _ in range(m):
                answer.pop()

if len(answer):
    print(''.join(answer))
else:
    print("FRULA")