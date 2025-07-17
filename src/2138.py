# 전구와 스위치
# https://www.acmicpc.net/problem/2138
# 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

def toggle(data, target):
    cnt = 0
    for i in range(1, n):
        if data[i - 1] == target[i - 1]:
            continue
        # toggle
        cnt += 1
        # 양 옆 전환
        for j in range(i - 1, i + 2):
            if j < n:
                data[j] = 1 - data[j]
    if data == target:
        return cnt
    return float('inf')

# 첫 번째 스위치를 누르지 않은 경우
answer = toggle(data[:], target)

# 첫 번째 스위치를 누른 경우
data[0] = 1 - data[0]
data[1] = 1 - data[1]

answer = min(answer, toggle(data, target) + 1)

if answer == float('inf'):
    print(-1)
else:
    print(answer)

