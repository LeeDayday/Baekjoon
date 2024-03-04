# 연구소
# https://www.acmicpc.net/problem/14502
# 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    global result
    tmp_graph = deepcopy(graph)
    queue = deepcopy(virus_pos)
    
    while queue:
        curr_i, curr_j = queue.popleft()
        for i in range(4):
            new_i = curr_i + dx[i]
            new_j = curr_j + dy[i]
            if new_i < 0 or new_j < 0 or new_i >= n or new_j >= m:
                continue
            # 빈 칸인 경우에 대해서만 탐색 진행
            if tmp_graph[new_i][new_j] == 0:
                queue.append((new_i, new_j))
                tmp_graph[new_i][new_j] = 2 # 감염 처리

    # 안전 영역 개수 구하기
    tmp_safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                tmp_safe_cnt += 1
    
    result = max(result, tmp_safe_cnt)
    

def make_wall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1 # 벽 세우기
                make_wall(wall_cnt + 1)
                graph[i][j] = 0 # 벽 해제  


def solution():
    global n, m, graph, virus_pos, result
    n, m = map(int, input().split())
    graph = []
    virus_pos = deque()
    for i in range(n):
        graph.append(list(map(int, input().split())))
        if 2 in graph[i]:
            # index 함수 사용 시, 만족하는 가장 첫번째 index만 반환
            # 따라서 for 문으로 모두 확인해줘야 함
            for j in range(m):
                if graph[i][j] == 2:
                    virus_pos.append((i, j))
    result = 0
    # 벽 만들기
    # 벽이 3개가 되면 bfs 수행 및 안전 영역 개수 구하기
    make_wall(0)
    return result


if __name__ == '__main__':
    print(solution())