# 수 묶기
# https://www.acmicpc.net/problem/1744
# 그리디 알고리즘, 정렬, 많은 조건 분기

# =======================================
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())

pos_data = []
neg_data = []

for _ in range(n):
    num = int(input())
    if num > 0:
        heappush(pos_data, -num) # max heap
    else:
        heappush(neg_data, num)

result = 0
while len(pos_data) > 1:
    a = -heappop(pos_data)
    b = -heappop(pos_data)
    if a + b < a * b:
        result += a * b
    else:
        result += a + b
if len(pos_data) == 1:
    result += -heappop(pos_data)

while len(neg_data) > 1:
    a = heappop(neg_data)
    b = heappop(neg_data)
    if a + b < a * b:
        result += a * b
    else:
        result += a + b

if len(neg_data) == 1:
    result += heappop(neg_data)

print(result)
