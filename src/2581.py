# 소수
# https://www.acmicpc.net/problem/2581
# 수학, 정수론, 소수 판정

# =======================================
import sys
import math
input = sys.stdin.readline

def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n = int(input())
m = int(input())

min_result = 10000
total_result = 0

for num in range(n, m + 1):
    if is_prime_number(num):
        min_result = min(min_result, num)
        total_result += num

if total_result == 0:
    print(-1)
else:
    print(total_result)
    print(min_result)