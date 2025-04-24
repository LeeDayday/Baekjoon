# ZAMKA
# https://www.acmicpc.net/problem/11874
# 수학, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

l = int(input())
d = int(input())
x = int(input())

def get_cnt(num):
    tmp = 0
    while num:
        tmp += num % 10
        num //= 10
    if tmp == x:
        return True
    return False

for num in range(l, d + 1):
    if get_cnt(num):
        print(num)
        break

for num in range(d, l - 1, -1):
    if get_cnt(num):
        print(num)
        break