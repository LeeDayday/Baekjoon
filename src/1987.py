# 알파벳
# https://www.acmicpc.net/problem/1987
# 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹, 격자 그래프

# =======================================
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, c = map(int, input().split())

data = []
for _ in range(r):
    data.append(list(input().rstrip()))

visited = set(data[0][0])
answer = 1
def dfs(x, y, result):

    global answer
    answer = max(answer, result)

    if answer == 26: # 가지치기, 더 이상의 탐색은 불필요
        return
    for i in range(4):
        new_x = x + dx[i]
        new_x, new_y = x + dx[i], y + dy[i]
        if 0 <= new_x < r and 0 <= new_y < c:
            if data[new_x][new_y] not in visited:
                visited.add(data[new_x][new_y])
                dfs(new_x, new_y, result + 1)
                visited.remove(data[new_x][new_y])

dfs(0, 0, answer)
print(answer)
