# 곱셈
# https://www.acmicpc.net/problem/1629
# 

# =======================================
import sys
input = sys.stdin.readline

# 분할 정복을 통해 거듭제곱을 구한다
# a^b = a^(b/2) * a^(b/2)
def power(a, n):
    if n == 1:
        return a % c
    else:
        # n이 짝수인 경우
        result = power(a, n//2)
        if n % 2 == 0:
            return result * result % c
        else:
            return result * result * a % c

a, b, c = map(int, input().split())

print(power(a, b))