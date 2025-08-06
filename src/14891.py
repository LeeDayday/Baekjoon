# 톱니바퀴
# https://www.acmicpc.net/problem/14891
# 구현, 시뮬레이션

# =======================================
import sys
from collections import defaultdict
input = sys.stdin.readline

indexes = [0] * 4 # 톱니바퀴 별 12시 방향의 index

data = defaultdict(list) # 톱니바퀴 정보
for i in range(4):
    data[i] = list(map(int, input().rstrip()))

answer = 0 # 최종 점수

def get_score(indexes:list[int]) -> int:
    score = 0
    for i in range(4):
        if data[i][indexes[i]] == 1:
            score += 2 ** i
    return score

def rotate(idx:int, dir:int, visited:list[bool], indexes:list[int]) -> None:
    # 더 이상 회전할 톱니바퀴가 없는 경우 종료
    if idx < 0 or idx > 3:
        return
    
    visited[idx] = True # 현재 톱니바퀴 방문 처리
    curr_9 = data[idx][(indexes[idx] - 2) % 8] # 현재 톱니바퀴의 9시 방향 극
    curr_3 = data[idx][(indexes[idx] + 2) % 8] # 현재 톱니바퀴의 3시 방향 극
    # 왼쪽에 미방문 톱니바퀴가 있는 경우
    
    if idx - 1 >= 0 and not visited[idx - 1]:
        # 왼쪽 톱니바퀴도 함께 돌아가는지 검사
        if curr_9 ^ data[idx - 1][(indexes[idx - 1] + 2) % 8]:
            rotate(idx - 1, -dir, visited, indexes)
    
    # 오른쪽에 미방문 톱니바퀴가 있는 경우
    if idx + 1 < 4 and not visited[idx + 1]:
        if curr_3 ^ data[idx + 1][(indexes[idx + 1] - 2) % 8]:
            rotate(idx + 1, -dir, visited, indexes)        
    
    # 톱니바퀴 0시 방향 idx 변경
    if dir == 1: # 시계 방향
        indexes[idx] = (indexes[idx] - 1) % 8
    else:
        indexes[idx] = (indexes[idx] + 1) % 8

for _ in range(int(input())):
    num, dir = map(int, input().split())
    visited = [False] * 4 
    rotate(num - 1, dir, visited, indexes)

print(get_score(indexes))