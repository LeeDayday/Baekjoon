# 복습 - 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
data = []
for _ in range(e):
    data.append(list(map(int, input().split())))

data.sort(key= lambda x: x[2])

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


def solution():
    answer = 0
    parent = [i for i in range(v + 1)]
    for s, e, weight in data:
        if find_parent(parent, s) != find_parent(parent, e):
            union(parent, s, e)
            answer += weight

    return answer

print(solution())


