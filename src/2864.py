# 5와 6의 차이
# https://www.acmicpc.net/problem/2864
# 수학, 그리디 알고리즘, 문자열, 사칙연산

# =======================================
import sys
input = sys.stdin.readline


def get_min(a, b):
    a = int(a.replace('6', '5'))
    b = int(b.replace('6', '5'))
    return a + b


def get_max(a, b):
    a = int(a.replace('5', '6'))
    b = int(b.replace('5', '6'))
    return a + b


if __name__ == '__main__':
    a, b = input().split()
    print(get_min(a, b), get_max(a, b))