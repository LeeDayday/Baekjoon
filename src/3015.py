# 오아시스 재결합
# https://www.acmicpc.net/problem/3015
# 자료구조, 스택
# =======================================
import sys

n = int(sys.stdin.readline())
heights = []
for _ in range(n):
    heights.append(int(sys.stdin.readline()))

stack = [] # (키, 연속으로 같은 횟수)
cnt = 0
for height in heights:
    # stack의 top값과 height을 비교하여 stack의 내림 차순 유지
    while stack and stack[-1][0] < height:
        cnt += stack.pop()[1]

    # stack이 비어있다면
    # cnt 값을 추가하지 않고 stack만 추가한다
    if not stack:
        stack.append((height, 1))
        continue

    # stack의 top과 height이 같다면
    # 앞에 연속된 같은 키 덩어리도 다 더한다
    if stack[-1][0] == height:
        eq_cnt = stack.pop()[1]
        cnt += eq_cnt
        if stack: cnt += 1
        stack.append((height, eq_cnt + 1))
    
    else:
        stack.append((height, 1))
        cnt += 1
    
print(cnt)
