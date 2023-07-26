# 소수 찾기
# https://www.acmicpc.net/problem/1978
# 수학, 정수론, 소수 판정

# =======================================
import sys

n = int(input())
numbers = tuple(map(int, input().split()))

def is_prime(num):
    if num == 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

cnt = 0
for num in numbers:
    cnt += is_prime(num)

print(cnt)