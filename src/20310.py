# 타노스
# https://www.acmicpc.net/problem/20310
# 그리디 알고리즘, 문자열

# =======================================
import sys
input = sys.stdin.readline

s = list(input().rstrip())

cnt_0 = 0

for ch in s:
    if ch == '0':
        cnt_0 += 1

idx = len(s) - 1
for i in range(cnt_0 // 2):
    while idx > 0 and s[idx] != '0':
        idx -= 1
    if idx > 0:
        s[idx] = '*'

idx = 0
for i in range((len(s) - cnt_0) // 2):
    while idx < len(s) and s[idx] != '1':
        idx += 1
    if idx < len(s):
        s[idx] = '*'


for i in range(len(s)):
    if s[i] != '*':
        print(s[i], end='')
