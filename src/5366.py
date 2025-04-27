# Total Count
# https://www.acmicpc.net/problem/5366
# 자료 구조, 해시를 사용한 집합과 맵

# =======================================
import sys
from collections import Counter
def input(): return sys.stdin.readline()


counter = Counter()
while True:
    data = input().rstrip()
    if data == '0':
        break
    counter[data] += 1

total = 0
for key, value in counter.items():
    total += value
    print(f"{key}: {value}")
print(f"Grand Total: {total}")
