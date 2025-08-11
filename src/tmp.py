# 복습 - 문서 검색
# https://www.acmicpc.net/problem/1543

# O(n)

import sys
input = sys.stdin.readline

data = input().rstrip()
target = input().rstrip()

n = len(data)
t = len(target)

i = 0
answer = 0
while i < n:
    if i + t <= n:
        if data[i:i + t] == target:
            answer += 1
            i += t
        else: i += 1
    else:
        break

print(answer)