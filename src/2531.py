# 회전 초밥
# https://www.acmicpc.net/problem/2531
# 브루트포스 알고리즘, 두 포인터, 슬라이딩 윈도우

# =======================================
import sys
from collections import Counter
input = sys.stdin.readline

n, d, k, c = map(int, input().split()) # 접시의 수, 초밥 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호

data = [] # 벨트 위 초밥 종류 
for _ in range(n):
    data.append(int(input()))

answer = 0

sushi = Counter() # 먹은 초밥 번호 및 개수
for i in range(k):
    sushi[data[i]] += 1

for i in range(n):
    # 쿠폰 초밥이 포함되어 있는 경우
    if sushi[c] != 0:
        answer = max(answer, len(sushi))
    else:
        answer = max(answer, len(sushi) + 1)
    # i 번째 스시 접시 제거
    sushi[data[i]] -= 1
    if sushi[data[i]] == 0:
       del sushi[data[i]]
    # (i + k) % n 번째 스시 접시 추가
    sushi[data[(i + k) % n]] += 1
    
print(answer)



