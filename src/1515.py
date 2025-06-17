# 수 이어 쓰기
# https://www.acmicpc.net/problem/1515
# 구현, 그리디 알고리즘, 문자열, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

data = input().rstrip()
n = 0
idx = 0

while True:
    n += 1
    for s in str(n):
        if data[idx] == s:
            idx += 1
            if idx >= len(data):
                print(n)
                exit()
