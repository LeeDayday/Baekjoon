# 캠핑
# https://www.acmicpc.net/problem/4796
# 수학, 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline


def get_cnt(l, p, v):
    x = v // p
    y = v % p
    if y < l:
        return l * x + y
    return l * x + l


if __name__ == '__main__':
    i = 0
    while True:
        l, p, v = map(int, input().split())
        if l == 0 and p == 0 and v == 0:
            break
        print(f"Case {i+1}: {get_cnt(l, p, v)}")
        i += 1
   