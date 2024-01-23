# 한조서열정리하고옴ㅋㅋ
# https://www.acmicpc.net/problem/14659
# 그리디 알고리즘

# =======================================
import sys
from collections import deque
input = sys.stdin.readline


def get_cnt(heights):
    max_cnt = 0
    while heights:
        cnt = 0
        tmp = heights.popleft()
        while heights:
            if tmp < heights[0]:
                break
            heights.popleft()
            cnt += 1
        max_cnt = max(cnt, max_cnt)
    return max_cnt


if __name__ == '__main__':
    n = int(input())
    heights = deque(list(map(int, input().split())))
    print(get_cnt(heights))