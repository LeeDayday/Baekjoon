# 주사위
# https://www.acmicpc.net/problem/1041
# 수학, 그리디 알고리즘

# =======================================
n = int(input())
arr = list(map(int, input().split()))
cnt = 0


# 한 면이 보이는 경우
min_1 = min(arr)

cnt += min_1*(5*(n-2)**2 + 4*(n-2))

# 두 면이 보이는 경우
min_2 = 100
for i in range(0, 5):
    for j in range(i+1, 6):
        if i + j != 5: # 평행하지 않은 두 면에 대한
            if min_2 > arr[i] + arr[j]: # 최솟값 구하기
                min_2 = arr[i] + arr[j]
cnt += min_2*(4*(n-2)+4*(n-1))

# 세 면이 보이는 경우
min_3 = 150
for i in [0, 5]:
    for j in [1, 4]:
        for k in [2, 3]:
            if min_3 > arr[i]+arr[j]+arr[k]:
                min_3 = arr[i]+arr[j]+arr[k]
cnt += min_3*4

# n이 1인 경우
if n==1:
    cnt = sum(arr) - max(arr)
print(cnt)