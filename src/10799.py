# 쇠막대기
# https://www.acmicpc.net/problem/10799
# 스택, 자료구조

# =======================================
import sys
input = sys.stdin.readline

data = input().rstrip()

stack = [] # stack엔 실시간 쇠막대기 개수만 관리
cnt = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if i > 0 and data[i-1] == '(': # 레이저인 경우
            cnt += len(stack)
        else: # 쇠막대기가 끝난 경우
            cnt += 1 # 잘리고 나머지 부분 (잘린 적이 없다면, 쇠막대기 한 덩어리 자체)

print(cnt)