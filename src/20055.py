# 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055
# 구현, 시뮬레이션

# =======================================
import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))

robots = [False] * n # 로봇 유무. 컨베이어 벨트 상단에만 로봇 존재하므로 범위는 n까지

# 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 1 감소

answer = 0

while k > 0:
    # 컨베이어 벨트 한 칸 회전 (로봇과 함께, 내구도 영향 없음)
    belt.appendleft(belt.pop())
    last = robots[-1]
    for i in range(n - 2, -1, -1):
        robots[i] = robots[i - 1]
    # 로봇 내리기
    robots[n - 1] = False

    # 로봇 이동 (로봇만, 내구도 1 감소)
    for i in range(n - 1, 0, -1):
        # [i-1] 에 있는 로봇이 [i] 로 이동할 수 있는지
        if not robots[i] and robots[i-1] and belt[i] > 0: # 로봇 존재 여부, 내구도 확인
            robots[i], robots[i - 1] = robots[i - 1], robots[i]
            belt[i] -= 1
            if belt[i] == 0:
                k -= 1
    # 로봇 내리기
    robots[n - 1] = False

    # 로봇 올리기
    if not robots[0] and belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            k -= 1
    #print(belt, robots)
    answer += 1

print(answer)




    # 올리는 위치에 있는 칸의 내구도가 0이 아니라면 로봇을 올린다
