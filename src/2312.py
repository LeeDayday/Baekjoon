# 수 복원하기
# https://www.acmicpc.net/problem/2312
# 수학, 정수론, 소수 판정, 에라토스테네스의 체

# =======================================
import sys
input = sys.stdin.readline


def solution(n):
    result = []
    for p in range(2, n + 1):
        cnt = 0
        while n % p == 0:
            cnt += 1
            n //= p
        if cnt:
            result.append([p, cnt])
    
    for p, cnt in result:
        print(p, cnt)


for _ in range(int(input())):
    solution(int(input()))