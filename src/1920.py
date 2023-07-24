# 수 찾기
# https://www.acmicpc.net/problem/1920
# 자료 구조, 정렬, 이분 탐색

# =======================================
import sys
input = sys.stdin.readline

def binarySearch(l, r, num):
    while l <= r:
        mid = (l+r)//2
        if num == arr1[mid]:
            return 1
        elif num < arr1[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return 0


if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr1.sort()

    m = int(input())
    arr2 = tuple(map(int, input().split()))

    for num in arr2:
        print(binarySearch(0, n-1, num))



    