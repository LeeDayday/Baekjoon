# 알고리즘 수업 - 퀵 정렬 1
# https://www.acmicpc.net/problem/24090
# 구현, 정렬

# =======================================
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def partition(arr, start, end):
    global cnt
    # pivot: arr[end]
    # arr[start:i] : pivot 이하의 수로만 이루어지도록 작업 예정
    i = start - 1 
    # j는 리스트를 훑으며 pivot 이하의 수가 있는지 확인
    for j in range(start, end):
        if arr[j] <= arr[end]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1 
            if cnt == k:
                print(arr[i], arr[j])

    # 마지막으로, pivot(arr[end]) 의 위치가 현재 위치에서 swap이 필요한지 확인
    if i + 1 != end:
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        cnt += 1
        if cnt == k:
            print(arr[i + 1], arr[end])

    return i + 1
        

def quick_sort(arr, start, end, k):
    if start < end:
        q = partition(arr, start, end)
        quick_sort(arr, start, q - 1, k)
        quick_sort(arr, q + 1, end, k)


cnt = 0
n, k = map(int, input().split())
arr = list(map(int, input().split()))
quick_sort(arr, 0, n - 1, k)
if cnt < k:
    print(-1)