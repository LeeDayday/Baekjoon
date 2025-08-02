# 스타트와 링크
# https://www.acmicpc.net/problem/14889
# 브루트포스 알고리즘, 백트래킹

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
numbers = [i for i in range(1, n + 1)]

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

min_gap = float('inf')
for start in combinations(numbers, n // 2):
    team = [0, 0]
    link = []
    for num in numbers:
        if num not in start:
            link.append(num)

   # print(start, link)
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            if i != j:
                team[0] += data[start[i] - 1][start[j] - 1] + data[start[j] - 1][start[i] - 1]
                team[1] += data[link[i] - 1][link[j] - 1] + data[link[j] - 1][link[i] - 1]
    #print(f"{team}")
    min_gap = min(min_gap, abs(team[0] - team[1]))

print(min_gap)
