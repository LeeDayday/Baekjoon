# 숨바꼭질
# https://www.acmicpc.net/problem/1697
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 100001
visited = [0] * MAX
visited[n] = 1

def BFS(n, k):
    queue = deque()
    queue.append(n)

    while queue:
        curr = queue.popleft()
        if curr == k:
            return visited[curr]
        for num in (curr-1, curr+1, curr*2):
            if num >= 0 and num < MAX:
                if visited[num] == 0:
                    # 방문 처리 (걸린 시간 저장)
                    visited[num] = visited[curr] + 1
                    queue.append(num)

    return visited[k]                      

print(BFS(n,k) - 1)
