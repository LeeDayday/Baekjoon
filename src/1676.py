# 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676
# 수학

# =======================================
import sys

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

n = int(sys.stdin.readline())

str_n = str(factorial(n))

cnt = 0
for ch in str_n[::-1]:
    if ch == '0':
        cnt += 1
    else:
        break

print(cnt)


