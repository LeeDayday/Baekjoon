# 약수 구하기
# https://www.acmicpc.net/problem/2501
# 수학, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0
# n의 약수 중, n을 제외한 가장 큰 약수는 항상 n // 2 이하임을 이용
for i in range(1, n // 2 + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    if cnt == k - 1:
        print(n)
    else:
        print(0)