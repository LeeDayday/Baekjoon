# 거북이
# https://www.acmicpc.net/problem/8911
# 구현, 시뮬레이션

# =======================================
import sys
input = sys.stdin.readline

move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 북, 동, 남, 서 전진
def solution(data):
    x, y = 0, 0
    x_set = set()
    y_set = set()
    x_set.add(x)
    y_set.add(y)
    
    move_idx = 0 # 초기 거북이 머리 방향: 북쪽
    
    for cmd in data:
        if cmd == 'F':
            x += move[move_idx][0]
            y += move[move_idx][1]
            x_set.add(x)
            y_set.add(y)
        elif cmd == 'B':
            x -= move[move_idx][0]
            y -= move[move_idx][1]
            x_set.add(x)
            y_set.add(y)
        elif cmd == 'L':
            move_idx = (move_idx - 1) % 4
        else:
            move_idx = (move_idx + 1) % 4
    print(x_set, y_set)
    return (abs(max(x_set) - min(x_set)) * abs(max(y_set) - min(y_set)))

for _ in range(int(input())):
    data = list(input().rstrip())
    print(solution(data))