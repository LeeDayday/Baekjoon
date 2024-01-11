# 알고리즘 수업 - 삽입 정렬 2
# https://www.acmicpc.net/problem/24052
# 구현, 정렬, 시뮬레이션

# =======================================
import sys
input = sys.stdin.readline

def insertion_sort(arr, n, k):
    cnt = 0
    for i in range(1, n):
        loc = i - 1
        new_item = arr[i]

        while (loc >= 0 and new_item < arr[loc]):
            arr[loc + 1] = arr[loc]
            cnt += 1
            if cnt == k:
                return arr
            loc -= 1

        if loc != i - 1:
            arr[loc+1] = new_item
            cnt += 1
            if cnt == k:
                return arr
    return [-1]

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(*insertion_sort(arr, n, k))

