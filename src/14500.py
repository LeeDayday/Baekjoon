# 테트로미노
# https://www.acmicpc.net/problem/14500
# 구현, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 종이 크기: n x m
n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

visited = [[False] * (m) for _ in range(n)]

# 테트로미노 모양: I, O, L, S, T
# T(ㅗ) 를 제외한 나머지 모양은 dfs(상하좌우 이동)를 연속 4번 수행했을 때 표현 가능한 모양
# [i][j] 를 기준으로 상하좌우 4번 이동시, 얻을 수 있는 최댓값 구하기
    # I, O, L, S 는 dfs 로 구현 가능
    # T는 별도로 구현

answer = 0
def dfs(x:int, y:int, result:int, cnt:int) -> None:
    global answer
    # dfs를 4번 실행했다면 종료
    if cnt == 4:
        answer = max(answer, result)
        return
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < m:
            if not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                dfs(new_x, new_y, result + data[new_x][new_y], cnt + 1)
                visited[new_x][new_y] = False
        else:
            continue

def check_t_shape(x:int, y:int) -> None:
    global answer
    # (ㅗ ㅏ ㅜ ㅓ) 중 최댓값은 + 에서 최솟값을 빼는 것, [x][y] 가 중심점
    elements = []
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < m:
            elements.append(data[new_x][new_y])
    
    if len(elements) == 4: # (ㅗ ㅏ ㅜ ㅓ) 모두 발생 가능한 경우
        elements.remove(min(elements))
        answer = max(answer, sum(elements) + data[x][y])
    elif len(elements) == 3: # T자형 최소 구성 요소를 만족한 경우
        answer = max(answer, sum(elements) + data[x][y])
    return 

for i in range(n):
    for j in range(m):
        # [i][j]에 테트로미노 놓기
        visited[i][j] = True
        dfs(i, j, data[i][j], 1) # I, O, L, S 모양 검사
        check_t_shape(i, j)# T 모양 검사
        visited[i][j] = False 
print(answer)