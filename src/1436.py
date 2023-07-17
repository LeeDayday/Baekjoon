# 영화감독 숌
# https://www.acmicpc.net/problem/1436
# 브루트포스 알고리즘

# =======================================
import sys

n = int(sys.stdin.readline())
num = 666
cnt = 0

def check_666(num):
    num = str(num)
    if "666" in num:
        return True
    else:
        return False

while True:
    if check_666(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    if cnt > n:
        break
    num += 1


