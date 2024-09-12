# 빗물
# https://www.acmicpc.net/problem/14719
# 구현, 시뮬레이션
# O(N)
# =======================================
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

# i번째 위치까지의 최대 높이
left_max = [0] * w # 0 ~ i 중 최대 높이
right_max = [0] * w # i ~ n-1 중 최대 높이


left_max[0] = heights[0] # 0 ~ 0 중 최대 높이는 자기 자신
for i in range(1, w):
    left_max[i] = max(left_max[i-1], heights[i])

right_max[-1] = heights[-1]
for i in range(w - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], heights[i])


# 빗물 양 계산하기
total = 0
for i in range(1, w-1): # 양 끝엔 빗물이 고일 수 없음
    compare = min(left_max[i], right_max[i])
    if compare > heights[i]:
        total += compare - heights[i]

print(total)