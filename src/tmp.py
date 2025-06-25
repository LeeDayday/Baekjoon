# 복습 - 숨바꼭질
# https://www.acmicpc.net/problem/1697

# O(V + E) => O(V + 3V) => O(V) (V 는 최대 100001)

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
visited = [False] * (100001)

# 동생 위치 > 수빈 위치 도달 bfs
queue.append((k, 0)) # 현재 위치, 시간
visited[k] = True

while queue:
    curr_pos, curr_time = queue.popleft()
    for next_pos in [curr_pos - 1, curr_pos + 1, curr_pos // 2 if curr_pos % 2 == 0 else -1]:
        if next_pos == n:
            print(curr_pos)
            exit(0)
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            queue.append((next_pos, curr_time + 1))
            visited[next_pos] = True
