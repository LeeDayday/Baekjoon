# 이진수
# https://www.acmicpc.net/problem/3460
# 수학, 구현

# =======================================
import sys
input = sys.stdin.readline

def get_binary(n):
    binary_number = ''
    while n != 0:
        r = n % 2
        binary_number = str(r) + binary_number
        n //= 2
    return binary_number

for _ in range(int(input())):
    n = int(input())
    result = get_binary(n)
    len_ = len(result)
    for i in range(1, len_ + 1):
        if result[len_ - i] == '1':
            print(i - 1, end=' ')
