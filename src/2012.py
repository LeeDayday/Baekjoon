# 등수 매기기
# https://www.acmicpc.net/problem/2012
# 그리디 알고리즘, 정렬
# =======================================
import sys

n = int(sys.stdin.readline())

arr = []
cnt = 0

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in range(0, n):
    cnt += abs(i+1 - arr[i])

print(cnt)