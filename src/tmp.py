# 복습 - 줄 세우기
# https://www.acmicpc.net/problem/2252

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = defaultdict(list)
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split()) # a가 b 앞에 서야 한다
    data[a].append(b) # 인접 리스트 추가
    indegree[b] += 1 # 진입 차수 추가

def solution():
    answer = []
    queue = deque()
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        # 진입 차수가 0인 정점 queue에 추가
        if indegree[i] == 0:
            queue.append(i)
        
    while queue:
        node = queue.popleft()
        answer.append(node)
        visited[node] = True
        for new_node in data[node]:
            if not visited[new_node]:
                indegree[new_node] -= 1
                if indegree[new_node] == 0:
                    queue.append(new_node)

    return answer
    

print(*solution())

