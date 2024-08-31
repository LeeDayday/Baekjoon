# 이진수
# https://www.acmicpc.net/problem/3460
# 수학, 구현

# =======================================
import sys
input = sys.stdin.readline

def get_binary(n):
    result = []
    power_of_two = 2 ** 19
    while power_of_two != 0:
        if n >= power_of_two:
            result.append(1)
            n -= power_of_two
        else:
            result.append(0)
        power_of_two //= 2
    idx = 0
    while result[idx] == 0:
        idx += 1
    return result[idx:]
# 13 = 8 + 4 + 1 = 1101
for _ in range(int(input())):
    n = int(input())
    result = get_binary(n)
    result = result[::-1]
    for i in range(len(result)):
        if result[i] == 1:
            print(i, end=' ')