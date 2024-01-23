# 컵홀더
# https://www.acmicpc.net/problem/2810
# 구현, 그리디 알고리즘, 문자열

# =======================================
import sys
input = sys.stdin.readline


def get_cnt(n, seats):
    l_cnt = seats.count('L')
    cup_cnt = n + 1 - l_cnt // 2
    print(min(n, cup_cnt))   
    

if __name__ == '__main__':
    n = int(input())
    seats = input().rstrip()
    get_cnt(n, seats)