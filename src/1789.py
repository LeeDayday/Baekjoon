# 수들의 합
# https://www.acmicpc.net/problem/1789
# 

# =======================================
import sys
input = sys.stdin.readline


def get_max(n):
    # 1 ~ n 까지의 합: n(n+1)/2
    num = 1
    while True:
        tmp = num * (num + 1) // 2
        if tmp + num < n:
            num += 1
            pass
        else:
            break
    print(num)

    
if __name__ == '__main__':
    n = int(input())
    get_max(n)