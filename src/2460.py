# 지능형 기차 2
# https://www.acmicpc.net/problem/2460
# 수학, 구현, 사칙연산

# =======================================
import sys
input = sys.stdin.readline

curr = 0
max_cnt = 0
for _ in range(10):
    minus, plus = map(int, input().split())
    curr += -minus + plus
    max_cnt = max(max_cnt, curr)
print(max_cnt)