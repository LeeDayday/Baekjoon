# 겹치는 건 싫어
# https://www.acmicpc.net/problem/20922
# 두 포인터

# =======================================
import sys
from collections import Counter
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
counter = Counter()
answer = 0
while start <= end and end < n:
    while end < n:
        if counter[data[end]] + 1 <= k:
            counter[data[end]] += 1
        else:
            break
        end += 1
    answer = max(answer, end - start)
    counter[data[start]] -= 1
    start += 1
    

print(answer)