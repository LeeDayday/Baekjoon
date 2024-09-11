# 오큰수
# https://www.acmicpc.net/problem/17298
# 자료 구조, 스택

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
result = [-1] * (n) # result[i]: data[i] 의 오큰수
stack = [0] # 오큰수를 구해야하는 data의 index 관리

for i in range(1, n):
    while stack and data[stack[-1]] < data[i]:
        result[stack.pop()] = data[i]
    stack.append(i)

print(*result)