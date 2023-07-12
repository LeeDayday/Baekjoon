# 선 긋기
# https://www.acmicpc.net/problem/2170
# 정렬, 스위핑

# =======================================
import sys
input = sys.stdin.readline

def find_length(lines, n):
    # x 좌표를 기준으로 lines 정렬
    lines.sort()
    # 기준 설정
    line_x, line_y = lines[0][0], lines[0][1]
    cnt = 0
    for i in range(1, n):
        # 선이 겹치는 경우 y 좌표 갱신
        if line_y >= lines[i][0]:
            line_y = max(line_y, lines[i][1])
        # 선이 겹치지 않는 경우, 기준 재설정
        else:
            cnt += line_y - line_x
            line_x, line_y = lines[i][0], lines[i][1]
            
    cnt += line_y - line_x

    return cnt

if __name__ == '__main__':
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(tuple(map(int, input().split())))

    print(find_length(lines, n))
    