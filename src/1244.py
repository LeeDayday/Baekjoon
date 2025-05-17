# 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244
# 구현, 시뮬레이션

# =======================================
import sys
input = sys.stdin.readline

n = int(input()) # 스위치 개수
data = list(map(int, input().split())) # 각 스위치 상태
toggle = {1: 0, 0: 1}

for _ in range(int(input())):
    gender, num = map(int, input().split())
    idx = 1
    if gender == 1: # 남자인 경우
        while num * idx - 1 < n: # 스위치 번호가 배수인 스위치 toggle
            data[num * idx - 1] = toggle[data[num * idx - 1]]
            idx += 1
    elif gender == 2: # 여자인 경우
        data[num - 1] = toggle[data[num - 1]]
        while True: # 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간 모두 toggle
            # data의 구간을 벗어난 경우
            if num - idx - 1 < 0 or num + idx - 1 >= n:
                break
            # 더 이상 대칭이 아닌 경우
            if data[num - idx - 1] != data[num + idx - 1]:
                break
            data[num - idx - 1] = toggle[data[num - idx - 1]]
            data[num + idx - 1] = toggle[data[num + idx - 1]]
            idx += 1

# 스위치 한 줄에 20개씩 출력
for i in range(n):
    print(data[i], end=" ")
    if (i + 1) % 20 == 0:
        print()