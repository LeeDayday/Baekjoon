# 우유 축제
# https://www.acmicpc.net/problem/14720
# 구현, 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline


def count_max(arr):
    cnt = 0
    for curr_milk in arr:
        if curr_milk == cnt % 3:
            cnt += 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_max(arr))