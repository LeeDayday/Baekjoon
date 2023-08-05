# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 수학, 문자열, 그리디 알고리즘, 파싱

# =======================================
import sys
input = sys.stdin.readline

# 뺄셈을 기준으로 식을 쪼갠다
math_str = input().rstrip().split('-')
result = 0

# 맨 처음 덧셈식 연산 처리 (+ 수행)
for num in math_str[0].split('+'):
    result += int(num)
# 나머지 식 연산 처리 (- 수행)
for num_str in math_str[1:]:
    # 덧셈을 기준으로 식 나눠서 뺄셈 수행
    for num in num_str.split('+'):
        result -= int(num)

print(result)
