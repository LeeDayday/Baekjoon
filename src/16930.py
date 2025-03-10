from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
start_x, start_y, goal_x, goal_y = map(lambda x: x - 1, map(int, input().split()))

def bfs():
    queue = deque([(start_x, start_y)])
    distance = [[float('inf')] * m for _ in range(n)]  # 거리를 무한대로 초기화
    distance[start_x][start_y] = 0  # 시작점 거리 0으로 설정

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        curr_x, curr_y = queue.popleft()

        for i in range(4):
            new_x, new_y = curr_x, curr_y

            for _ in range(k):
                new_x += dx[i]
                new_y += dy[i]

                # 범위를 벗어나거나 벽(#)을 만나면 중단
                if not (0 <= new_x < n and 0 <= new_y < m) or graph[new_x][new_y] == '#':
                    break
                # 갱신할 필요가 없는 경우
                if distance[new_x][new_y] <= distance[curr_x][curr_y]:
                    break
                # 갱신 및 큐에 추가
                if distance[new_x][new_y] == float('inf'):
                    distance[new_x][new_y] = distance[curr_x][curr_y] + 1
                    queue.append((new_x, new_y))

    return distance[goal_x][goal_y] if distance[goal_x][goal_y] != float('inf') else -1

print(bfs())
