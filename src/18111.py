# 마인크래프트
# https://www.acmicpc.net/problem/18111
# 구현, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = []

min_h = 64000000
max_h = 1
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        min_h = min(graph[i][j], min_h)
        max_h = max(graph[i][j], max_h)    

result = []
for height in range(max_h, min_h - 1, -1):
    cnt = 0
    blocks = b
    flag = 0
    for i in range(n):
        if flag:
            break
        for j in range(m):
            current_h = graph[i][j]
            # 블록을 제거해야 하는 경우
            if height < current_h:
                cnt += 2 * (current_h - height)
                blocks += current_h - height
            # 블록을 쌓아야하는 경우
            elif height > current_h:
                cnt += height - current_h
                blocks -= height - current_h
    if blocks < 0:
        flag = 1
    if flag == 0:        
        result.append((cnt, height))

result.sort(key=lambda x: (x[0], -x[1]))

print(result[0][0], result[0][1])
