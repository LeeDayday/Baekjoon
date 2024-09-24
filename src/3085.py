# 사탕 게임
# https://www.acmicpc.net/problem/3085
# 구현, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))


def get_max_cnt(graph):
    result = 0
    # 행 확인
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if graph[i][j] == graph[i][j + 1]:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 1
        result = max(result, cnt)
    # 열 확인
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if graph[j][i] == graph[j + 1][i]:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 1
        result = max(result, cnt)

    return result

cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(2):
            if i + dx[k] < n and j + dy[k] < n:
                if graph[i][j] == graph[i + dx[k]][j + dy[k]]:
                    continue
                # 사탕 교환
                graph[i][j], graph[i + dx[k]][j + dy[k]] = graph[i + dx[k]][j + dy[k]], graph[i][j]
                # 먹을 수 있는 사탕 개수 구하기
                cnt = max(cnt, get_max_cnt(graph))
                # 사탕 원위치
                graph[i][j], graph[i + dx[k]][j + dy[k]] = graph[i + dx[k]][j + dy[k]], graph[i][j]

            else:
                continue

print(cnt)