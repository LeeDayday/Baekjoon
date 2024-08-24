# Divisors
# https://www.acmicpc.net/problem/13225
# 수학, 구현, 브루트포스 알고리즘, 사칙연산

# =======================================
import sys
input = sys.stdin.readline

def process(n):
    cnt = 1
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            cnt += 1
    return cnt

for _ in range(int(input())):
    n = int(input())
    print(n, process(n))