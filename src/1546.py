# 평균
# https://www.acmicpc.net/problem/1546
# 수학, 사칙연산

# =======================================
import sys

input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

for i in range(n):
    scores[i] = scores[i] / max_score * 100

print(round(sum(scores)/n, 6))