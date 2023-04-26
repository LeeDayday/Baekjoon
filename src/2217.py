# 로프
# https://www.acmicpc.net/problem/2217
# 수학, 그리디 알고리즘, 정렬

# =======================================
import sys

n = int(sys.stdin.readline())
weights = []

for i in range(n):
    weights.append(int(sys.stdin.readline()))

weights.sort(reverse=True)

for i in range(n):
    weights[i] *= (i+1)

print(max(weights))