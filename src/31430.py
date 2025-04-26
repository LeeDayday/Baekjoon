# A+B - 투 스텝
# https://www.acmicpc.net/problem/31340
# 수학, 구현, 문자열

# =======================================
import sys
input = sys.stdin.readline

def dec_to_str(num):
    result = ''
    while num:
        num, r = divmod(num, 26)
        result += chr(ord('a') + r)
    return "a" * (13 - len(result)) + result[::-1] # 'a': 0이므로 값에 영향을 주지 않음. padding으로도 활용

def str_to_dec(data):
    result = 0
    for i in range(13):
        result *= 26
        result += int(ord(data[i]) - ord('a'))
    return result

t = int(input())

if t == 1:
    a, b = map(int, input().split())
    print(dec_to_str(a + b))
elif t == 2:
    data = input()
    print(str_to_dec(data))

