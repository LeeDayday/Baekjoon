# 복습 - 부분합
# https://www.acmicpc.net/problem/1806

import sys
input = sys.stdin.readline

n, s = map(int, input().split()) # n: 수열의 길이, s: 부분합 기준
data = list(map(int, input().split())) # 수열

def solution(n, s, data):
    answer = float('inf')
    start, end = 0, 0
    cnt = data[start] # 누적합 (=sum(data[start:end]))
    while end < n:
        if cnt < s:
            end += 1
            if end < n:
                cnt += data[end]
        else:
            answer = min(answer, end - start + 1)
            cnt -= data[start]
            start += 1
    
    if answer == float('inf'):
        return 0
    return answer

print(solution(n, s, data))


