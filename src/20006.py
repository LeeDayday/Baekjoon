# 랭킹전 대기열
# https://www.acmicpc.net/problem/20006
# 구현, 시뮬레이션

# =======================================
import sys
input = sys.stdin.readline

p, m = map(int, input().split()) # p: 플레이어의 수, m: 방의 정원

members = []
for _ in range(p):
    level, nickname = input().split()
    members.append([int(level), nickname])

rooms = [] # rooms[i]: [기준 level, [방에 들어간 인원 정보]]
for level, nickname in members:
    for i in range(len(rooms)):
        # 방의 정원이 가득 찬 경우
        if len(rooms[i][1]) == m:
            continue
        # 들어갈 수 있는 방이 있다면 입장
        if rooms[i][0] - 10 <= level <= rooms[i][0] + 10:
            rooms[i][1].append([level, nickname])
            break
    # 들어갈 수 있는 방이 없다면 새로운 방 생성
    else:
        rooms.append([level, [[level, nickname]]])

for i in range(len(rooms)):
    # 방의 정원이 가득 찬 경우
    if len(rooms[i][1]) == m:  
        print("Started!")
    else:
        print("Waiting!")
    rooms[i][1].sort(key=lambda x: x[1])
    for info in rooms[i][1]:
        print(info[0], info[1])
