# 복습 - 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

# O((N-1)!)

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
operators = list(map(int, input().split())) # 연산자 [+,  -,  x,  //] 의 개수

answer = [-float('inf'), float('inf')] # max, min
def dfs(idx:int, total:int, plus:int, minus:int, mul:int, div:int) -> None:
    global answer
    if idx == n: # 연산 수행 종료
        answer[0] = max(total, answer[0])
        answer[1] = min(total, answer[1])
        return
    if plus:
        dfs(idx + 1, total + data[idx], plus - 1, minus, mul, div)
    if minus:
        dfs(idx + 1, total - data[idx], plus, minus - 1, mul, div)

    if mul:
        dfs(idx + 1, total * data[idx], plus, minus, mul - 1, div)

    if div:
        if total < 0:
            dfs(idx + 1, -(-total // data[idx]), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, total // data[idx], plus, minus, mul, div - 1)


dfs(1, data[0], *operators)

for ans in answer:
    print(ans)
