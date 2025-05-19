# 어두운 굴다리
# https://www.acmicpc.net/problem/17266
# 구현, 이분 탐색

# =======================================
import sys
input = sys.stdin.readline

n = int(input()) # 굴다리의 길이
m = int(input()) # 가로등의 개수
data = list(map(int, input().split())) # 설치할 수 있는 가로등 위치

answer = 1
while True:
    # 첫번째 가로등이 초반 영역을 밝히지 못하는 경우
    if data[0] - answer > 0:
        answer += 1
        continue
    # 마지막 가로등이 마지막 영역을 밝히지 못하는 경우
    if data[-1] + answer < n:
        answer += 1
        continue
    # 그 외 영역을 모두 밝히는지 확인
    for i in range(m - 1):
        if i + 1 < m and data[i] + answer >= data[i + 1] - answer:
            continue
        else:
            answer += 1
            break
    else:
        break

print(answer)