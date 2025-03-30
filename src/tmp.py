# 복습 - 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
time = [float('inf')] * 100001
cnt = [0] * 100001

queue = deque([n])
time[n] = 0

while queue:
    curr_pos = queue.popleft()
    if curr_pos == k:
        break
    # 1초가 소요되는 이동
    for next_pos in (curr_pos - 1, curr_pos + 1):
        if 0 <= next_pos < 100001:
            # 더 빠른 시간으로 방문하는 경우 (업데이트 필요)
            if time[next_pos] > time[curr_pos] + 1:
                time[next_pos] = time[curr_pos] + 1
                queue.append(next_pos)
    # 0초가 소요되는 이동
    next_pos = curr_pos * 2
    if 0 <= next_pos < 100001:
        # 더 빠른 시간으로 방문하는 경우 (업데이트 필요)
        if time[next_pos] > time[curr_pos]:
            time[next_pos] = time[curr_pos]
            queue.append(next_pos)
            cnt[next_pos] = cnt[curr_pos]
        # 동일한 시간으로 방문하는 경우 (cnt ++)
        elif time[next_pos] == time[curr_pos]:
            cnt[next_pos] += cnt[curr_pos]      

print(time[k])
