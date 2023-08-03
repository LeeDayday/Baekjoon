# 리모컨
# https://www.acmicpc.net/problem/1107
# 

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
_ = int(input())
# 정상 작동하는 버튼의 집합
btns = tuple(map(int, input().split()))

# 최솟값 초기값: 100에서 목표 채널까지 이동한 수
min_count = abs(100 - n)

# 모든 경우의 수 탐색
for channel in range(1000001):
    channel = str(channel)
    flag = 0
    for ch in channel:
        # 고장난 버튼이 있다면 break
        if int(ch) in btns:
            flag = 1
            break
    # 정상 작동한 버튼으로 만들어진 채널인 경우
    # 최솟값 비교
    if flag == 0:
        min_count = min(min_count, abs(int(channel) - n) + len(channel))

print(min_count)
        

