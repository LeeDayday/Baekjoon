# 피보나치 수 5
# https://www.acmicpc.net/problem/10870
# 수학, 구현

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

if n < 2:
    print(n)
    exit(0)

pibo = [0] * (n+1)
pibo[1] = 1

for i in range(2, n+1):
    pibo[i] = pibo[i-1] + pibo[i-2]

print(pibo[n])
