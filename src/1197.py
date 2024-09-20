# 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197
# 그래프 이론, 최소 스패닝 트리

# =======================================
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
v, e = map(int, input().split())
edges = []

for _ in range(v):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x:x[2]) # weight 기준 오름차순 정렬

parent = [i for i in range(v + 1)]
result = 0
for start, end, weight in edges:
    # 사이클이 발생하지 않는 경우에만 트리 집합에 포함
    if find_parent(parent, start) != find_parent(parent, end):
        result += weight
        union(parent, start, end)        

print(result)
