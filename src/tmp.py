# 복습 - 바이러스
# https://www.acmicpc.net/problem/2606

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
m = int(input())

data = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

def solution():
    cnt = 0
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    while queue:
        node = queue.popleft()
        for new_node in data[node]:
            if not visited[new_node]:
                cnt += 1
                visited[new_node] = True
                queue.append(new_node)
    return cnt

print(solution())