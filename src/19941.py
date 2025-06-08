# 햄버거 분배
# https://www.acmicpc.net/problem/19941
# 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
data = list(input().rstrip())

answer = 0
for i in range(n):
    if data[i] == 'P':
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and data[j] == 'H':
                data[j] = 'X'
                answer += 1
                break

print(answer)
