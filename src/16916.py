# 부분 문자열
# https://www.acmicpc.net/problem/16916
# 구현, 문자열

# =======================================
import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

if p in s:
    print(1)
else:
    print(0)