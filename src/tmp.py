# 복습 - 단어 공부
# https://www.acmicpc.net/problem/1157

# O(N)

import sys
from collections import Counter
input = sys.stdin.readline

data = input().rstrip()

counter = Counter(data.upper())

max_count = -1
max_char = ''
duplicate = False

for char, cnt in counter.items():
    if cnt > max_count:
        max_count = cnt
        max_char = char
        duplicate = False
    elif cnt == max_count:
        duplicate = True

if duplicate:
    print("?")
else:
    print(max_char)