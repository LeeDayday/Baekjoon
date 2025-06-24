# 볼 모으기
# https://www.acmicpc.net/problem/17615
# 그리디 알고리즘

# =======================================
import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
data = input().rstrip()

# direction 방향으로 target 색 공 옮기기
def solution(s, direction, target):
    # direction 방향에 있는 target 색 덩어리는 제거
    if direction == 'left':
        s = s.lstrip(target)
    else:
        s = s.rstrip(target)
    # 남은 target 색 공 반환 (옮겨야 하는 공 개수)
    return s.count(target)

print(min(solution(data, 'left', 'R'), solution(data, 'left', 'B'), solution(data, 'right', 'R'), solution(data, 'right', 'B')))
