# 폴리오미노
# https://www.acmicpc.net/problem/1343
# 구현, 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline
    

def get_polyomino(str):
    str = str.replace('XXXX', 'AAAA')
    str = str.replace('XX', 'BB')
    if 'X' in str:
        print("-1")
    else:
        print(str)

if __name__ == '__main__':
    str = input().rstrip()
    get_polyomino(str)