# 스타트와 링크
# https://www.acmicpc.net/problem/14889
# 브루트포스 알고리즘, 백트래킹

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
numbers = [i for i in range(1, n + 1)]

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

visited = [False] * n
answer = float('inf')

def dfs(cnt, idx):
    global answer
    if answer == 0:
        return
    # 팀 구성이 이루어진 경우
    if cnt == n // 2:
        score = [0, 0] # 팀 1, 팀 2의 총점
        for i in range(n):
            for j in range(i + 1, n):
                # i, j 모두 스타트 팀인 경우 
                if visited[i] and visited[j]:
                    score[0] += data[i][j] + data[j][i]
                # i, j 모두 링크 팀인 경우
                elif not visited[i] and not visited[j]:
                    score[1] += data[i][j] + data[j][i]
        answer = min(answer, abs(score[0] - score[1]))
        return
    
    # 팀 구성이 이루어지지 않은 경우
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True # i 번째 팀원을 스타트 팀에 포함
            dfs(cnt + 1, i + 1)
            visited[i] = False # 백 트래킹

visited[0] = True
dfs(1, 1)
print(answer)

