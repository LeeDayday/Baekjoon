# 수들의 합 2
# https://www.acmicpc.net/problem/2003
# 브루트포스 알고리즘, 누적 합, 두 포인터

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

l, r = 0, 0
total = data[0] # 초기 부분합
answer = 0 # 경우의 수

while r < n:
    if total < m:
        r += 1
        if r < n:
            total += data[r]
    else:
        if total == m:
            answer += 1
        total -= data[l]
        l += 1

print(answer)