# 문자열 교환
# https://www.acmicpc.net/problem/1522
# 문자열, 브루트포스 알고리즘, 재귀

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

# T -> S
# 방법 1: 맨 뒤가 A 라면, 맨 뒤 A pop
# 방법 2: 맨 앞이 B 라면, 맨 앞 B pop & 뒤집기
def dfs(t):
    if t == s:
        print(1)
        exit(0)
    if len(t) == 0:
        return 0
    if t[-1] == 'A': # 방법 1
        dfs(t[:-1])
    if t[0] == 'B': # 방법 2
        dfs(t[-1:0:-1])
dfs(t)
print(0)