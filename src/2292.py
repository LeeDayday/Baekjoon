# 벌집
# https://www.acmicpc.net/problem/2292
# 수학

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
max_num = 1

while n > max_num:
    max_num += 6 * cnt
    cnt += 1

print(cnt)
