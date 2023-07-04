# 문서 검색
# https://www.acmicpc.net/problem/1543
# 그리디 알고리즘, 정렬

# =======================================
import sys
input = sys.stdin.readline

# 팀의 수
n = int(input())
# 코딩 역량
total_power = list(map(int, input().split()))

total_power.sort()

i = 0
j = len(total_power) - 1
result = 200000

while True:
    if i >= j:
        break
    result = min(result, total_power[i] + total_power[j])
    i += 1
    j -= 1

print(result)
