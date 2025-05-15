# 쿠키의 신체 측정
# https://www.acmicpc.net/problem/20125
# 구현

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(input().rstrip()))

# 심장 위치 찾기
found = False
heart = [0, 0]
for i in range(n):
    for j in range(n):
        # 처음 * 등장 위치: 머리
        if data[i][j] == '*':
            heart[0] = i + 1
            heart[1] = j
            found = True
            break
    if found:
        break

print(heart[0] + 1, heart[1] + 1) # 심장 위치 출력

result = [0, 0, 0, 0, 0]
# 왼쪽 팔 길이 계산
col = heart[1] - 1
while col >= 0 and data[heart[0]][col] == '*':
    col -= 1
    result[0] += 1
   
# 오른쪽 팔 길이 계산
col = heart[1] + 1
while col < n and data[heart[0]][col] == '*':
    col += 1
    result[1] += 1

# 허리 계산
w_row = heart[0] + 1
while w_row < n and data[w_row][heart[1]] == '*':
    w_row += 1
    result[2] += 1

# 왼쪽 다리 계산
row = w_row 
while row < n and data[row][heart[1] - 1] == '*':
    row += 1
    result[3] += 1

# 오른쪽 다리 계산
row = w_row 
while row < n and data[row][heart[1] + 1] == '*':
    row += 1
    result[4] += 1

print(*result)