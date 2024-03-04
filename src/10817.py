# 세 수
# https://www.acmicpc.net/problem/10817
# 구현, 정렬

# =======================================
import sys
input = sys.stdin.readline

def solution():
    arr = list(map(int, input().split()))
    arr.sort()
    return arr[1]    

if __name__ == '__main__':
    print(solution())