# ZOAC 4
# https://www.acmicpc.net/problem/23971
# 수학, 사칙연산

# =======================================
import sys
from math import ceil
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

print(ceil(h / (n + 1)) * ceil(w / (m + 1)))
