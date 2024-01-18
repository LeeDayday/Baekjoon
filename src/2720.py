# 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720
# 수학, 그리디 알고리즘, 사칙연산

# =======================================
import sys
input = sys.stdin.readline


def get_count(num):
    coins = [25, 10, 5, 1]
    result = []
    for coin in coins:
        cnt = 0
        if num // coin:
            cnt += num // coin
            num %= coin
        result.append(cnt)
    return result
        

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(*get_count(int(input())))
