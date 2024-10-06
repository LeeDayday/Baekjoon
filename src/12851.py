# 숨바꼭질 2
# https://www.acmicpc.net/problem/12851
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque()
queue.append((n, 0)) #위치, 걸리는 시간

cnt = [[-1, 0] for _ in range(100001)]  # (최단 시간, 방법의 수)
# 초기값 설정
cnt[n][0] = 0
cnt[n][1] = 1

while queue:
    loc, time = queue.popleft()
    
    next_locs = [loc - 1, loc + 1, loc * 2]
        
    for next_loc in next_locs:
        if 0 <= next_loc <= 100000:
            # 최단 시간을 갱신하는 경우 (해당 위치에 처음 도달하는 경우)
            if cnt[next_loc][0] == -1:
                cnt[next_loc][0] = time + 1
                cnt[next_loc][1] = cnt[loc][1]
                queue.append((next_loc, time + 1))
            # 최단 시간과 같은 경우
            elif cnt[next_loc][0] == time + 1:
                cnt[next_loc][1] += cnt[loc][1]

print(cnt[k][0])
print(cnt[k][1])