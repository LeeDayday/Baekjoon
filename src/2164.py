# 카드2
# https://www.acmicpc.net/problem/2164
# 자료 구조, 큐

# =======================================
import sys
from collections import deque

n = int(input())
cards = deque(list(i for i in range(1, n+1)))

# 카드가 한 장 남으면 종료
while len(cards) > 1:
    # 제일 위에 있는 카드를 버린다
    cards.popleft()
    # 제일 위에 있는 카드를 제일 뒤로
    cards.append(cards.popleft())  

print(cards[0])
