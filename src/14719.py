# 빗물
# https://www.acmicpc.net/problem/14719
# 구현, 시뮬레이션

# =======================================
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

total = 0 # 빗물의 총량

for i in range(1, w - 1): # 양 끝에는 빗물이 고일 수 없으므로 제외
    max_height_left = max(heights[:i])
    max_height_right = max(heights[i+1:])
    # heights[i] 에서 빗물이 고일 수 있는지 확인
    compare_height = min(max_height_left, max_height_right)
    if heights[i] < compare_height:
        total += compare_height - heights[i]
print(total)