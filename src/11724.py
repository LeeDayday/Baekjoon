from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, visited):
    queue = deque()
    queue.append(i)
    # 방문 처리
    visited[i] = True
    # queue가 빌 때까지 인접한 노드 방문하기
    while queue:
        num = queue.popleft()
        for i in graph[num]:
            # 미방문 인접 노드 방문하기
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)] # idx는 1부터 유의미

# 인접 리스트 생성
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (n+1)
cnt = 0

for i in range(1, n+1):
    # 방문하지 않은 노드에 대하여
    if not visited[i]:
        # 인접한 노드가 있으면
        if graph[i]:
            # bfs 수행
            bfs(i, visited)
            cnt += 1
        # 혼자 독립된 노드라면 (인접한 노드가 없다면)
        else:
            visited[i] = True # 방문처리
            cnt += 1

print(cnt)

