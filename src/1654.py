# 랜선 자르기
# https://www.acmicpc.net/problem/1654
# 이분 탐색, 매개 변수 탐색

# =======================================
import sys
input = sys.stdin.readline

def find_max(arr):
    arr.sort()
    start = 1
    end = arr[-1]

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for num in arr:
            cnt += num // mid
        if cnt < n:
            end = mid - 1
        else:
            start = mid + 1

    return end

if __name__ == '__main__':
    k, n = map(int, input().split())
    lan_list = []
    for _ in range(k):
        lan_list.append(int(input()))
    print(find_max(lan_list))