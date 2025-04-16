# 삼삼한 수
# https://www.acmicpc.net/problem/17252
# 수학, 사칙연산

# =======================================
import sys
input = sys.stdin.readline

data = int(input())

def solution(data):
    if data == 0:
        return "NO"
    while data > 0:
        if data % 3 != 0 and data % 3 != 1:
            return "NO"
        data //= 3
    return "YES"
        
print(solution(data))
