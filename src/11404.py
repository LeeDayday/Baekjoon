# 플로이드
# https://www.acmicpc.net/problem/11404
# 그래프 이론, 플로이드-워셜

# =======================================
import sys
from math import inf
input = sys.stdin.readline

def floydWarshall():
    # 정점 i를 거쳐가는 경우
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


n = int(input())
m = int(input())

graph = [[inf for _ in range(n)] for _ in range(n)] # idx 1부터 유의미한 값

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

# 시작 도시와 도착 도시가 같은 경우는 없다
for i in range(n):
    graph[i][i] = 0

floydWarshall()

for i in range(n):
    for j in range(n):
        if graph[i][j] == inf:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

