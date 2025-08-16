# 근손실
# https://www.acmicpc.net/problem/18429

# 브루트포스 알고리즘, 백트래킹

import sys
from itertools import permutations
input = sys.stdin.readline

# n일 동안 n개의 운동 키트 수행
# 매일 k만큼 근손실
n, k = map(int, input().split())
data = list(map(int, input().split()))

answer = 0
for kits in permutations(data, n):
    weight = 500
    for kit in kits:
        weight -= k
        weight += kit
        if weight < 500:
            break
    else:
        answer += 1

print(answer)