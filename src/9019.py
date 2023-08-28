# DSLR
# https://www.acmicpc.net/problem/9019
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline


def find_dslr(a, b):
    queue = deque()
    queue.append([a, ''])
    visited[a] = True

    while queue:
        num, cmd = queue.popleft()
        if num == b:
            print(cmd)
            break

        tmp = (num * 2) % 10000
        if visited[tmp] is False:
            queue.append([tmp, cmd+'D'])
            visited[tmp] = True

        tmp = (num - 1) % 10000
        if visited[tmp] is False:
            queue.append([tmp, cmd+'S'])
            visited[tmp] = True

        tmp = (num // 1000) + (num % 1000) * 10
        if visited[tmp] is False:
            queue.append([tmp, cmd+'L'])
            visited[tmp] = True

        tmp = (num // 10) + (num % 10) * 1000
        if visited[tmp] is False:
            queue.append([tmp, cmd+'R'])
            visited[tmp] = True

        
if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())

        visited = [False for _ in range(10001)]
        find_dslr(a, b)