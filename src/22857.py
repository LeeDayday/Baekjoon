# 가장 긴 짝수 연속한 부분 수열 (small)
# https://www.acmicpc.net/problem/22857
# 다이나믹 프로그래밍, 두 포인터

# =======================================
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n: 수열의 길이, k: 삭제할 수 있는 최대 횟수
s = list(map(int, input().split()))

start = 0
answer = 0
cnt = 0

for end in range(n):
    if s[end] % 2 == 1:
        cnt += 1
    while cnt > k:
        if s[start] % 2 == 1:
            cnt -= 1
        start += 1

    answer = max(answer, end - start + 1 - cnt)

print(answer)