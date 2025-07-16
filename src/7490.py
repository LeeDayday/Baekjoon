# 0 만들기
# https://www.acmicpc.net/problem/7490
# 구현, 문자열, 브루트포스 알고리즘, 백트래킹

# =======================================
import sys
input = sys.stdin.readline

def solution(num, end, result):
    if num == end:
        
        if eval(result.replace(' ', '')) == 0:
            print(result)
        return
    # 공백인 경우
    solution(num + 1, end, result + ' ' + str(num + 1))
    # + 인 경우
    solution(num + 1, end, result + '+' + str(num + 1))
    # - 인 경우
    solution(num + 1, end, result + '-' + str(num + 1))
    
for _ in range(int(input())):
    n = int(input())
    solution(1, n, '1')
    print()