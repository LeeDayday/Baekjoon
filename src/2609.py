# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
# 수학, 정수론, 유클리드 호제법

# =======================================
import sys
input = sys.stdin.readline

def find_gcd(n, m):
    num = 2
    result = 1
    while num <= min(n, m):
        if n % num == 0 and m % num == 0:
            result = num
        num += 1
    return result

def find_lcm(n, m):
    num = max(n, m)
    while True:
        if num % n == 0 and num % m == 0:
            return num
        num += 1


n, m = map(int, input().split())

print(find_gcd(n, m))
print(find_lcm(n, m))