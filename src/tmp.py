# 복습 - 수들의 합
# https://www.acmicpc.net/problem/1789

import sys
input = sys.stdin.readline

s = int(input())

def solution(s):
    # 1 ... n 까지의 합: (n * (n + 1)) / 2
    answer = 1
    while answer * (answer + 1) // 2 + answer < s:
        answer += 1

    return answer
    
print(solution(s))
