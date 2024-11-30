# 별 찍기 - 10
# https://www.acmicpc.net/problem/2447
# 분할 정복, 재귀

# =======================================
import sys
input = sys.stdin.readline

def solution(n):
    if n == 3:
        return ["***", "* *", "***"]
    
    pattern = solution(n // 3)
    result = []

    for row in pattern:
        result.append(row * 3)

    for row in pattern: # 비어있는 구간 표시
        result.append(row + " " * (n // 3) + row)

    for row in pattern:
        result.append(row * 3)

    return result

n = int(input())

result = solution(n)

for r in result:
    print(r)