# 스카이라운 쉬운거
# https://www.acmicpc.net/problem/1863
# 자료 구조, 스택

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    data.append(int(input().split()[1]))
data.append(0)

stack = []
answer = 0

for height in data:
    while stack and stack[-1] > height:
        stack.pop()
        answer += 1
    if not stack or stack[-1] < height:
        stack.append(height)

print(answer)
