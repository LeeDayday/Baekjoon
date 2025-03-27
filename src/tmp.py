# 복습 - 바이러스
# https://www.acmicpc.net/problem/2606

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())

data = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

def solution():
    cnt = 0
    stack = [1]
    visited = [False] * (n + 1)
    
    while stack:
        print(stack)
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            cnt += 1
            for new_node in data[node]:
                if not visited[new_node]:
                    stack.append(new_node)
    return cnt - 1

print(solution())