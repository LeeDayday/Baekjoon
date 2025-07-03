# 복습 - 탑
# https://www.acmicpc.net/problem/2493

# O(N)

import sys
input = sys.stdin.readline

n = int(input()) # 탑의 개수
data = list(map(int, input().split()))

answer = [0] * n

stack = []
for i in range(n):
    while stack and data[stack[-1]] <= data[i]:
        stack.pop()
    if stack and data[stack[-1]] > data[i]:
        answer[i] = stack[-1] + 1
    stack.append(i)
print(*answer)