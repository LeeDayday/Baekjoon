# 접두사
# https://www.acmicpc.net/problem/1141
# 그리디 알고리즘, 문자열 ,정렬

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    data.append(input().rstrip())

data.sort(key=len)

result = 0
for i in range(n):
    for j in range(i + 1, n):
        if data[i] == data[j][0:len(data[i])]:
            break
    else:
        result += 1

print(result)
