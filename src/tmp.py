# 복습 - 부분합
# https://www.acmicpc.net/problem/1806

# O(N)


import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
answer = float('inf')
sum_ = 0
while end < n:
    if sum_ < s:
        sum_ += data[end]
        end += 1
    else:
        answer = min(answer, end - start)
        sum_ -= data[start]
        start += 1

while sum_ >= s:
    answer = min(answer, end - start)
    sum_ -= data[start]
    start += 1    
if answer == float('inf'):
    print(0)
else:
    print(answer)
