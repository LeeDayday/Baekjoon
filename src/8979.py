# 올림픽
# https://www.acmicpc.net/problem/8979
# 구현, 정렬

# =======================================
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n: 국가의 수, k: 등수를 알고 싶은 국가
data = []

for _ in range(n):
    data.append(list(map(int, input().split()))) # 국가 id, 금, 은, 동 입력

data.sort(key=lambda x: (-x[1], -x[2], -x[3]))

def solution():
    rank = 1
    for i in range(n):
        if i > 0 and data[i][1:] != data[i - 1][1:]: # 동점자 존재 (rank 갱신 x)
            rank = i + 1
        if data[i][0] == k:
            return rank
    
print(solution())