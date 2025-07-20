# 좋다
# https://www.acmicpc.net/problem/1253
# 자료 구조, 정렬, 이분 탐색, 두 포인터

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

if n <= 2:
    print(0)
    exit(0)

answer = 0

for i in range(n):
    target = data[i]
    start = 0
    end = n - 1
    while start < end:
        if data[start] + data[end] == target:
            # 자기 자신인 경우는 제외해야 함
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                break
        elif data[start] + data[end] < target:
            start += 1
        else:
            end -= 1

print(answer)