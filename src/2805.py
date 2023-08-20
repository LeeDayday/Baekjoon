# 나무 자르기
# https://www.acmicpc.net/problem/2805
# 이분 탐색, 매개 변수 탐색

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = tuple(map(int, input().split()))

start = 1
end = max(heights)

while start <= end:
    mid_height = (start + end) // 2

    cnt = 0
    for height in heights:
        if height > mid_height:
            cnt += height - mid_height
    
    # 높이의 최댓값을 원하므로, 조건을 만족해도(적어도 m미터 충족) start 값을 오른쪽 범위로
    if cnt >= m:
        start = mid_height + 1
    else:
        end = mid_height - 1

print(end)
    
