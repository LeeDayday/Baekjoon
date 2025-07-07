# 틱택토
# https://www.acmicpc.net/problem/7682
# 구현, 많은 조건 분기

# =======================================
import sys
input = sys.stdin.readline

def is_finished(data, player):
    # 가로/세로 3칸 검사
    cnt = 0
    for x in range(3):
        if data[x * 3] == data[x * 3 + 1] == data[x * 3 + 2] == player:
            return True
        if data[x] == data[x + 3] == data[x + 6] == player:
            return True
    # 대각선 검사
    if data[0] == data[4] == data[8] == player:
        return True
    if data[2] == data[4] == data[6] == player:
        return True
    return False

while True:
    data = input().rstrip()
    if data == 'end':
        break
    result = [False, False]
    result[0] = is_finished(data, 'X')
    result[1] = is_finished(data, 'O')

    count = [data.count('X'), data.count('O')]
    if count[0] == count[1]: # 마지막 말이 O인 경우
        if not result[0]: # X에서 이미 결과가 나오지 않으면 정상
            if result[1] or data.count('.') == 0:
                print("valid")
                continue
    elif count[0] == count[1] + 1: # 마지막 말이 X인 경우
        if not result[1]: # O에서 이미 결과가 나오지 않으면 정상
            if result[0] or data.count('.') == 0:
                print("valid")
                continue
    print("invalid")

