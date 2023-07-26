# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
# 구현, 자료구조, 큐

# =======================================
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
result = []
idx = 0
while arr:
    idx += k - 1
    if idx >= len(arr):
        idx %= len(arr)

    result.append(arr.pop(idx))

    
print("<" + ", ".join(str(x) for x in result) + ">")