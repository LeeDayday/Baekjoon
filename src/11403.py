# 경로 찾기
# https://www.acmicpc.net/problem/11403
# 그래프 이론, 그래프 탐색, 플로이드-워셜

# =======================================
import sys
input = sys.stdin.readline

def floydWarshall():
    # 정점 i를 거쳐가는 경우
    for i in range(n):
        # j -> i -> k 가 가능한지 검사
        for j in range(n):
            for k in range(n):
                # j -> i -> k 가 가능한 경우, j -> k 도 가능
                if graph[j][i] * graph[i][k]:
                    graph[j][k] = 1


n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

floydWarshall()

for i in range(n):
    print(*graph[i])