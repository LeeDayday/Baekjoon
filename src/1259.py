# 팰린드롬수
# https://www.acmicpc.net/problem/1259
# 구현, 문자열

# =======================================
import sys
input = sys.stdin.readline

def check_palindrome(n):
    i = 0
    j = len(n) - 1
    while i < j:
        if n[i] != n[j]:
            return "no"
        i += 1
        j -= 1
    return "yes"

if __name__ == '__main__':
    while True:
        n = input().rstrip()
        if n == '0':
            exit()
        print(check_palindrome(n))