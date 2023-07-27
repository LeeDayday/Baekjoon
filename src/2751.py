# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
# 정렬

# =======================================
import sys
input = sys.stdin.readline

def merge(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
        
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

def mergesort(arr):
    # 더 이상 쪼갤 수 없는 경우
    if len(arr) <= 1:
        return arr
    
    # list 반으로 쪼개기
    mid = len(arr)//2
    
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))


if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(int(input()))

    arr = mergesort(arr)
    for num in arr:
        print(num)
