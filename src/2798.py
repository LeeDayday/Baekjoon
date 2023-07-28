# 블랙잭
# https://www.acmicpc.net/problem/2798
# 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = tuple(map(int, input().split()))
result = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            cnt = cards[i] + cards[j] + cards[k]
            if m - cnt < m - result and m - cnt >= 0:
                result = cnt


print(result)