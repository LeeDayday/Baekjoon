# 소트
# https://www.acmicpc.net/problem/1083
# 그리디 알고리즘, 정렬

# =======================================
n = int(input())
arr = list(map(int, input().split()))
s = int(input())
cnt = 0

for i in range(n-1):
    if s == 0:
        break
    max, idx = arr[i], i
    for j in range(i+1, s+i+1): # swap 가능한 범위 내 최댓값 찾기
        if j == n:
            break
        if max < arr[j]:
            max, idx = arr[j], j

    # 한 칸씩 뒤로 밀려난다
    for j in range(idx, i, -1):
        arr[j] = arr[j-1]
    arr[i] = max

    s -= idx - i # 교환 횟수


for i in arr:
    print(i, end=' ')
