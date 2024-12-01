# 로또
# https://www.acmicpc.net/problem/6603
# 수학, 조합론, 백트리킹, 재귀

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline

numbers = [i for i in range(1, 50)]

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    data = data[1:]
    result = []
    for comb in combinations(data, 6):
            result.append(comb)
    result.sort()

    for r in result:
        print(*r)
    print()


