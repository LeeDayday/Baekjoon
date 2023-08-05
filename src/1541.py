# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 

# =======================================
import sys
input = sys.stdin.readline

# 뺄셈을 기준으로 식을 쪼갠다
math_str = input().rstrip().split('-')

result = 0

for idx in range(len(math_str)):
    # 쪼갠 식에 + 가 있을 경우, + 연산을 한다
    # (덧셈 식을 하나의 연산 결과로 만드는 작업)
    flag = 0
    if '+' in math_str[idx]:
        flag = 1
        plus_cnt = 0 # 덧셈 최종값
        plus_str = math_str[idx].split('+') # 덧셈 기준으로 식 쪼개기
        for plus in plus_str:
            plus_cnt += int(plus)

    # math_str[idx] 가 덧셈식인 경우
    if flag:
        # 맨 처음 숫자라면 더해준다
        if idx == 0:
            result += plus_cnt
        # 그 외의 경우, 빼준다
        else:
            result -= plus_cnt
    # math_str[idx] 가 단일 숫자인 경우
    else:
        # 맨 처음 숫자라면 더해준다
        if idx == 0:
            result += int(math_str[idx])
        # 그 외의 경우, 뺴준다
        else:
            result -= int(math_str[idx])

print(result)
