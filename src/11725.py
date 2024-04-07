# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
# 그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색

# =======================================
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find_child(graph, parent, p_num):
    child_list = []
    for child in graph[p_num]:
        if parent[child] == 0:
            child_list.append(child)
            parent[child] = p_num
    for child in child_list:
        find_child(graph, parent, child)


def solution():
    n = int(input())
    graph = [[]for _ in range(n+1)]
    parent = [0 for _ in range(n+1)]
    parent[1] = 1 # 트리의 루트: 1

    for _ in range(n-1):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    find_child(graph, parent, 1)

    for i in range(2, n+1):
        print(parent[i])


if __name__ == '__main__':
    solution()