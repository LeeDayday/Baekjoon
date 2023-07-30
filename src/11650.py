# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
# 정렬

# =======================================
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(tuple(map(int, input().split())))

    graph.sort(key=lambda x : (x[0], x[1]))

    for i in range(n):
        print(graph[i][0], graph[i][1])