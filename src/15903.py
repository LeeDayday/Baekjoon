# 카드 합체 놀이
# https://www.acmicpc.net/problem/15903
# 자료 구조, 그리디 알고리즘, 우선순위 큐

# =======================================
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tmp = list(map(int, input().split()))
cards = []

for num in tmp:
    heappush(cards, num)
for _ in range(m):
    a = heappop(cards)
    b = heappop(cards)
    for _ in range(2):
        heappush(cards, a + b)

print(sum(cards))