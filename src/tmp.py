# 복습 - 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928

# O(V + E), (V:100, E: (100x6) + (n+m))


import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 사다리 개수, m: 뱀 개수

ladders = defaultdict(int)
for _ in range(n):
    start, end = map(int, input().split())
    ladders[start] = end

snakes = defaultdict(int)
for _ in range(m):
    start, end = map(int, input().split())
    snakes[start] = end

# 1부터 100까지의 게임판
data = [0 for _ in range(101)] # data[i]: i번째 칸 가는데 필요한 주사위 횟수
visited = [False for _ in range(101)] # i번째 칸 방문 여부

def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        curr_pos = queue.popleft()
        # 주사위 1부터 6까지
        for step in range(1, 7): 
            next_pos = curr_pos + step
            # 범위를 벗어나는 경우, 반복문 종료
            if curr_pos + step > 100:
                break
            # basecase: 정확히 100번째 칸에 도달한 경우
            if next_pos == 100:
                data[100] = data[curr_pos] + 1
                return
            if not visited[next_pos]:
                # 최종 도착점 계산 
                while True:
                    # next_pos 에 사다리가 있는 경우, 사다리까지 타기
                    if next_pos in ladders.keys():
                        next_pos = ladders[next_pos]
                    # next_pos에 뱀이 있는 경우, 뱀까지 타기
                    elif next_pos in snakes.keys():
                        next_pos = snakes[next_pos]
                    else:
                        break
                # 사다리/뱀을 모두 고려한 최종 도착점 비용 갱신
                if not visited[next_pos]:
                    visited[next_pos] = True
                    data[next_pos] = data[curr_pos] + 1
                    queue.append(next_pos)
            
bfs(1)
print(data[-1])