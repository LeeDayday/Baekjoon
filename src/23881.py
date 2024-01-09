# 알고리즘 수업 - 선택 정렬 1
# https://www.acmicpc.net/problem/23881
# 구현, 정렬, 시뮬레이션

# =======================================
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0 # swap 되는 횟수
# 최댓값부터 리스트 맨 뒤로 (선택 정렬)
for i in range(n-1, 0, -1):
    max_idx = i
    for j in range(i, -1, -1):
        if arr[max_idx] < arr[j]:
            max_idx = j
    if max_idx != i:
        arr[max_idx], arr[i] = arr[i], arr[max_idx] # swap
        cnt += 1
    if cnt == k:
        break

if cnt < k:
    print(-1)
else:
    print(arr[max_idx], arr[i])