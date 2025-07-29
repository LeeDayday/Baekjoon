# 복습 - 시험 감독
# https://www.acmicpc.net/problem/13458

# O(N)

import sys
input = sys.stdin.readline

n = int(input()) # 시험장 개수
data = list(map(int, input().split())) # 각 시험장에 있는 응시자 수
b, c = map(int, input().split()) # 총감독관/부감독관이 한 시험장에서 감시할 수 있는 응시자 수

answer = 0
for num in data:
    answer += 1
    num -= b
    if num > 0:
        answer += num // c
        if num % c != 0:
            answer += 1


print(answer)