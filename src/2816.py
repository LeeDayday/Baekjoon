# 디지털 티비
# https://www.acmicpc.net/problem/2816
# 구현, 해 구성하기

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(input().rstrip())

idx_1 = data.index('KBS1')
idx_2 = data.index('KBS2')

if idx_1 > idx_2: # KBS1 을 올리면서 KBS2가 내려간 경우
    idx_2 += 1

print('1' * (idx_1) + '4' * (idx_1) + '1' * (idx_2) + '4' * (idx_2 - 1))