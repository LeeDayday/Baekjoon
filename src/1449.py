# 수리공 항승
# https://www.acmicpc.net/problem/1449
# 그리디 알고리즘, 정렬

# =======================================
import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    n, l = map(int, input().split())
    pos = list(map(int, input().split()))
    pos.sort()
    pos = deque(pos)

    cnt = 0
    while pos:
        curr_pos = pos.popleft() # 새로운 테이프 시작점
        cnt += 1
        while pos:
            next_pos = pos[0]
            if next_pos - curr_pos < l:
                pos.popleft()
            else:
                break

    print(cnt)
