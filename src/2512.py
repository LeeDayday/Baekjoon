# 예산
# https://www.acmicpc.net/problem/2512
# 이분 탐색, 매개 변수 탐색

# =======================================
import sys
input = sys.stdin.readline

n = int(input()) # 지방의 수
data = list(map(int, input().split())) # 지방의 예산 요청
m = int(input()) # 총 예산

start = 1
end = max(data)

answer = 0
while start <= end:
    mid = (start + end) // 2 # 가정한 총 예산 최대 비용
    total = 0
    for budget in data:
        if budget > mid:
            total += mid
        else:
            total += budget
    if total <= m:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
