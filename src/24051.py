# 알고리즘 수업 - 삽입 정렬 1
# https://www.acmicpc.net/problem/24051
# 구현, 정렬, 시뮬레이션

# =======================================
import sys
input = sys.stdin.readline

def insertion_sort(arr, n, k):
    cnt = 0
    for i in range(1, n):
        loc = i - 1
        new_item = arr[i]
        # arr[0...i-1] 까진 오름차순으로 정렬이 된 상태
        # new_item이 들어갈 위치 찾기
        while (loc >= 0 and new_item < arr[loc]):
            arr[loc+1] = arr[loc] # 한 칸씩 뒤로 미루기
            cnt += 1
            if cnt == k:
                print(arr[loc+1]) # k번째 저장되는 수 출력
                return
            loc -= 1

        if loc != i-1:
            arr[loc+1] = new_item
            cnt += 1
            if cnt == k:
                print(arr[loc+1])
                return
            
    print(-1)    

n, k = map(int, input().split())
arr = list(map(int, input().split()))

insertion_sort(arr, n, k)