# 복습 - 등수 구하기
# https://www.acmicpc.net/problem/1205

# O(NlogN)


import sys
input = sys.stdin.readline

n, target, p = map(int, input().split())

if n == 0:
    print(1)
    exit(0)
data = list(map(int, input().split()))

data.append(target)
data.sort(reverse=True)

answer = data.index(target) + 1

if (answer > p) or (n == p and data[-1] == target): # 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 좋을 때만 점수가 바뀐다
    print(-1)
else:
    print(answer)
    