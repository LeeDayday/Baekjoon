# 좌표 압축
# https://www.acmicpc.net/problem/18870
# 정렬, 값/ 좌표압축

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
arr = tuple(map(int, input().split()))

result = []
for idx, value in enumerate(arr):
    result.append([value, idx])

result.sort()

# 압축 전 좌표값
tmp = result[0][0]
# 좌표값 중 최솟값은 0으로 압축됨
result[0][0] = 0
# 앞으로 압축될 좌표값
new_value = 0

# 좌표 압축 진행
for i in range(1, n):
    # 이전 좌표와 값이 같은 경우
    if tmp == result[i][0]:
        result[i][0] = new_value
    # 값이 다른 경우, 새로운 좌표값으로 압축 진행
    else:
        tmp = result[i][0]
        new_value += 1
        result[i][0] = new_value

# index 값을 기준으로 정렬
result.sort(key= lambda x: x[1])

for i in range(n):
    print(result[i][0], end=' ')

