# 블로그
# https://www.acmicpc.net/problem/21921
# 누적 합, 슬라이딩 윈도우

# =======================================
import sys
input = sys.stdin.readline

n, x = map(int, input().split()) # 전체 n일, 최대 누적 기간: x일
data = list(map(int, input().split()))

max_visitors = 0 # x일 동안 가장 많이 들어온 방문자 수
max_cnt = 0 # 위 조건을 만족한 기간 개수

start, end = 0, 0

tmp_visitors = 0
while start < n:
    while end < n and start + x != end:
        tmp_visitors += data[end]
        end += 1
    if tmp_visitors > max_visitors:
        max_visitors = tmp_visitors
        max_cnt = 1
    elif max_visitors != 0 and tmp_visitors == max_visitors:
        max_cnt += 1

    tmp_visitors -= data[start]
    start += 1

if max_cnt == 0:
    print("SAD")
else:
    print(max_visitors)
    print(max_cnt)