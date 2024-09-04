# N번째 큰 수
# https://www.acmicpc.net/problem/2693
# 정렬

# =======================================
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    print(a[-3])