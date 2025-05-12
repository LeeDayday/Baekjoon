# 덩치
# https://www.acmicpc.net/problem/7568
# 구현, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

rank = [1] * n

for i in range(n):
    for j in range(n):
        if i != j and data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank[i] += 1

print(*rank)