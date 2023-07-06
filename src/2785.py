# 체인
# https://www.acmicpc.net/problem/2785
# 그리디 알고리즘, 정렬

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
chains = list(map(int, input().split()))

chains.sort()

cnt = 0

while n > 1:
    min_chain = chains.pop(0)
    while min_chain > 0:
        # 1개의 체인으로 체인묶음 2개 연결 가능
        if min_chain == 1:
            n -= 2
        else:
            n -= 1
        min_chain -= 1
        cnt += 1
        if n <= 1:
            break

print(cnt)

