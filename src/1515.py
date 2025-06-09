# 수 이어 쓰기
# https://www.acmicpc.net/problem/1515
# 

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
