# 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 데이크스트라, 최단 경로, 0-1 너비 우선 탐색

# =======================================
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

dx = [1, -1]

def dijkstra(position, n, k):
    q = []
    # 시작 위치 초기화
    position[n] = 0
    heappush(q, (0, n))
    while q:
        curr_time, curr_pos = heappop(q)
        if curr_pos == k:
            print(position[k])
            return
        # +1, -1 이동
        for i in range(2):
            n_pos = curr_pos + dx[i]
            if n_pos >= 0 and n_pos <= 100000:
                n_time = curr_time + 1
                if position[n_pos] > n_time:
                    position[n_pos] = n_time
                    heappush(q, (n_time, n_pos))

        # *2 이동
        n_pos = curr_pos * 2
        if n_pos >= 0 and n_pos <= 100000:
            if position[n_pos] > curr_time:
                position[n_pos] = curr_time
                heappush(q, (curr_time, n_pos))
        

def solution():
    n, k = map(int, input().split())
    position = [INF] * (100001)
    dijkstra(position, n, k)


if __name__ == '__main__':
    solution()