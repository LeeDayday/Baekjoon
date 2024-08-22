# 약수 구하기
# https://www.acmicpc.net/problem/2501
# 수학, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        break

if cnt < k:
    print(0)
else:
    print(i)