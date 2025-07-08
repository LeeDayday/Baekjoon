# 숫자고르기
# https://www.acmicpc.net/problem/2668
# 그래프 이론, 그래프 탐색, 깊이 우선 탐색

# =======================================
import sys
input = sys.stdin.readline

n = int(input()) 

data = [0] + [int(input()) for _ in range(n)]
answer = []

def solution(node, visited, result):
    visited[node] = True
    if not visited[data[node]]:
        solution(data[node], visited, result)
    elif data[node] in result: # 사이클이 발생한 경우
        answer.extend(result[result.index(data[node]):]) # 사이클이 발생한 부분만 최종 결과에 추가
    
answer = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    solution(i, visited, [i])


print(len(answer))
for num in sorted(answer):
    print(num)