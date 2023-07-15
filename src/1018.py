# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
# 

# =======================================
import sys
input = sys.stdin.readline

def check_color(chess, start_i, start_j, color):
    cnt = 0
    first_color = color # 기준이 되는 색
    for i in range(start_i, start_i+8):
        # 첫째 줄은 인자로 전달된 color를 기준으로
        if i > start_i: 
            if (i - start_i) % 2 == 0:
                color = first_color
            else:
                color = 'W' if first_color == 'B' else 'B'
        for j in range(start_j, start_j+8):
            # 기준과 일치하지 않는다면 cnt + 1
            if chess[i][j] != color:
                cnt += 1
            color = 'W' if color == 'B' else 'B'
    return cnt

if __name__ == '__main__':
    n, m = map(int, input().split())
    chess = []
    for _ in range(n):
        chess.append(list(input().rstrip()))
    
    min_cnt = 64
    
    for i in range(n):
        if i + 8 > n:
            break
        for j in range(m):
            if j + 8 > m:
                break
            min_cnt = min(min_cnt, check_color(chess, i, j, 'W'), check_color(chess, i, j, 'B'))

    print(min_cnt)