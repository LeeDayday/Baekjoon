# Gerrymandering
# https://www.acmicpc.net/problem/17587
# 구현

# =======================================
from math import floor
import sys
from collections import defaultdict
input = sys.stdin.readline

p, d = map(int, input().split()) # 지역구, 지역
data = defaultdict(lambda: [0, 0])

for _ in range(p):
    d_i, vote_a, vote_b = map(int, input().split())
    data[d_i][0] += vote_a
    data[d_i][1] += vote_b

total_votes = 0

def get_waste_votes(a, b):
    vote = a + b
    target = floor(vote / 2) + 1
    if a < b:
        return "B", a, b - target, vote
    return "A", a - target, b, vote
    
total_votes = total_waste_a = total_waste_b = 0
for key in sorted(data.keys()):
    value = data[key]
    win_p, w_a, w_b, total = get_waste_votes(value[0], value[1])
    print(win_p, w_a, w_b)
    total_votes += total
    total_waste_a += w_a
    total_waste_b += w_b

print(f"{(abs((total_waste_a - total_waste_b)) / total_votes):.10f}")