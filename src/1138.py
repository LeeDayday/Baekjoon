# 한 줄로 서기
# https://www.acmicpc.net/problem/1138
# 구현, 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

answer = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == data[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1

print(*answer)