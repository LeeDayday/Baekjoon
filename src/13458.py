# 시험 감독
# https://www.acmicpc.net/problem/13458
# 수학, 사칙연산

# =======================================
import sys
from math import ceil
input = sys.stdin.readline

n = int(input()) # 시험장 개수
people = list(map(int, input().split())) # 시험장 당 응시자 수
b, c = map(int, input().split()) # b: 총감독관의 시험장 당 감독가능한 응시자 수, c: 부감독관의 시험장 당 감독가능한 응시자 수

answer = 0
for p in people:
    p -= b
    answer += 1
    if p > 0:
        answer += ceil(p / c)
print(answer)
