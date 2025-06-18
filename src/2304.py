# 창고 다각형
# https://www.acmicpc.net/problem/2304
# 구현, 자료 구조, 브루트포스 알고리즘, 스택

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split()))) # (x, y) 입력

# x 좌표 기준으로 정렬
graph.sort(key=lambda x: x[0])

# 가장 높은 기둥
max_x, max_y = max(graph, key=lambda x: x[1])

# 왼 -> 오
answer = 0
left_max = graph[0][1]
left_x = graph[0][0]
for x, y in graph:
    answer += (x - left_x) * left_max
    if y > left_max:
        left_max = y
    left_x = x
    if x == max_x:
        break

# 오 -> 왼
right_max = graph[-1][1]
right_x = graph[-1][0]
for x, y in reversed(graph):
    answer += (right_x - x) * right_max
    if y > right_max:
        right_max = y
    right_x = x
    if x == max_x:
        break

# 가장 높은 기둥 영역 더하기
answer += max_y
print(answer)
