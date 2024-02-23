# 카드 정렬하기
# https://www.acmicpc.net/problem/1715
# 자료 구조, 그리디 알고리즘, 우선순위 큐

# =======================================
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    cards = []
    for _ in range(n):
        heappush(cards, int(input()))
    total = 0
    while cards:
        card1 = heappop(cards)
        try:
            card2 = heappop(cards)
            total = total + card1 + card2
            heappush(cards, card1+card2)
        except:
            total += card1
    print(total-card1)

