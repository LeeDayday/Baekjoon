# 복습 - 등수 구하기
# https://www.acmicpc.net/problem/1205

# O(N)

import sys
input = sys.stdin.readline

n, target, p = map(int, input().split())

if n == 0:
    print(1)
    exit(0)
data = list(map(int, input().split()))

# 랭킹 리스트가 꽉 찼을 때 (n == p), 새 점수가 이전 점수보다 더 좋을 때만 점수 바뀜
if n == p and target == data[-1]:
    print(-1)
    exit(0)

# target 에 대한 등수 구하기
rank = 1
for score in data:
    if target < score:
        rank += 1
    else:
        break

# 해당 등수가 랭킹 리스트(p) 에 들 수 있다면 출력
if rank <= p:
    print(rank)
else:
    print(-1)
        

