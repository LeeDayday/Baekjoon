# IOIOI
# https://www.acmicpc.net/problem/5525
# 문자열

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

pn = "IOI" + ("OI"*(n-1))
# Pn => Pn-1 이 2개, Pn-2가 3개, ... 의 규칙을 가지고 있음
idx = 0
total = 0
while idx < m - 1:
    if s[idx] == 'O':
        idx += 1
        continue
    cnt = 0
    idx += 1
    # OI가 연속해서 나오는 횟수를 구한다
    while True:
        # idx가 범위 밖인 경우 반복문 종료
        if idx + 1 >= m:
            break
        if s[idx:idx+2] == 'OI':
            cnt += 1
            idx += 2
        else:
            break
    # cnt =>  Pcnt
    if cnt >= n:
        total += cnt - n + 1

print(total)
