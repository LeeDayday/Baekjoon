# 복습 - 문서 검색
# https://www.acmicpc.net/problem/1543

# O(n^2)

import sys
input = sys.stdin.readline

data = input().rstrip()
target = input().rstrip()

n = len(data)
t = len(target)
answer = 0
for i in range(n):
    j = i
    cnt = 0
    while j < n:
        if j + t <= n:
            if data[j:j + t] == target:
                cnt += 1
                j += t
            else: j += 1
        else:
            break
    answer = max(answer, cnt)

print(answer)