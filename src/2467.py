# 용액
# https://www.acmicpc.net/problem/2467
# 이분 탐색, 두 포인터

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

start, end = 0, n - 1
min_value = float('inf')
answer = [0, 0]
while start < end:
    result = data[start] + data[end]
    if abs(result) < min_value:
        min_value = abs(result)
        answer[0] = data[start]
        answer[1] = data[end]
    if result > 0:
        # 양수 값 줄이기
        end -= 1
    else:
        # 음수 값 줄이기
        start += 1
    
print(*answer)