# 이항 계수 1
# https://www.acmicpc.net/problem/11050
# 수학, 구현, 조합론

# =======================================
import sys

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

n, k = map(int, sys.stdin.readline().split())

print(factorial(n) // factorial(n-k) // factorial(k))