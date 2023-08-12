# 색종이 만들기
# https://www.acmicpc.net/problem/2630
# 분할 정복, 재귀

# =======================================
import sys
input = sys.stdin.readline
blue_cnt = 0
white_cnt = 0

def check_color(start_i, start_j, n):
    color_cnt = 0
    for i in range(n):
        color_cnt += sum(graph[start_i+i][start_j:start_j+n])
    # 모두 흰색인 경우
    if color_cnt == 0:
        return 0
    # 모두 파란색인 경우
    elif color_cnt == n ** 2:
        return 1
    # 모두 같은 색으로 칠해져 있지 않은 경우
    else:
        return -1
def divide_to_four(start_i, start_j, n):
    # 더 이상 쪼갤 수 없는 경우
    global blue_cnt
    global white_cnt

    if n == 1:
        if graph[start_i][start_j] == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
        return None
    

    half_len = n // 2

    dx = [start_i, start_i, start_i + half_len, start_i + half_len]
    dy = [start_j, start_j + half_len, start_j, start_j + half_len]
    # 분할 전 색 확인
    result = check_color(start_i, start_j, n)
    if result != -1:
        if result == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
        return
        
    # 4분면으로 분할
    for i in range(4):
        result = check_color(dx[i], dy[i], half_len)
        if result == 0:
            white_cnt += 1
        elif result == 1:
            blue_cnt += 1
        else:
            divide_to_four(dx[i], dy[i], half_len)



n = int(input())

graph = []
for _ in range(n):
    graph.append(tuple(map(int, input().split())))
divide_to_four(0, 0, n)
print(white_cnt)
print(blue_cnt)