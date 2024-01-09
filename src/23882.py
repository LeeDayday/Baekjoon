# 알고리즘 수업 - 선택 정렬 2
# https://www.acmicpc.net/problem/23882
# 구현, 정렬, 시뮬레이션

# =======================================
import sys

input = sys.stdin.readline

def selection_sort(arr, n, k):
    cnt = 0
    for i in range(n-1, 0, -1):
        last = i
        for j in range(i, -1, -1):
            if arr[last] < arr[j]:
                last = j
        if last != i:
            arr[last], arr[i] = arr[i], arr[last]
            cnt += 1
        if cnt == k:
            print(*arr)
            return
    print(-1)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

selection_sort(arr, n, k)