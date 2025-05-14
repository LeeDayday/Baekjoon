# 임스와 함께하는 미니게임
# https://www.acmicpc.net/problem/25757
# 자료 구조, 문자열, 해시를 사용한 집합과 맵

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline

n, game = input().split()

people = {
    'Y': 2,
    'F': 3,
    'O': 4
}

data = set()
for _ in range(int(n)):
    data.add(input().rstrip())

print(len(data) // (people[game] - 1))