# 부분합
# https://www.acmicpc.net/problem/1806
# 누적 합, 두 포인터

# =======================================
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
data = list(map(int, input().split()))

left, right = 0, 0
length = 100000001 # 부분합 길이
total = 0

while True:
    if total >= s:
        length = min(length, right - left)
        total -= data[left]
        left += 1
    elif right == n:
        break
    else:
        total += data[right]
        right += 1


if length > n:
    print(0)
else:
    print(length)