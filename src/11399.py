# ATM
# https://www.acmicpc.net/problem/11399
# 그리디, 정렬

# =======================================
import sys
input = sys.stdin.readline

def get_min(n, arr):
    result = 0
    arr.sort()

    for num in arr:
        result += num * n
        n -= 1
    
    print(result)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    get_min(n, arr)