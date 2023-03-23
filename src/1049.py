# 기타줄
# https://www.acmicpc.net/problem/1049
# 수학, 그리디 알고리즘

# =======================================
n, m = map(int, input().split())
arr = []
min_pack = 1000
min_nonpack = 1000
for i in range(m):
    arr.append(list(map(int, input().split()))) # 패키지(6개) 가격, 낱개 가격
    if min_pack > arr[i][0]:
        min_pack = arr[i][0]
    if min_nonpack > arr[i][1]:
        min_nonpack = arr[i][1]

N = n
if N // 6:
    cnt1 = min_pack * (N // 6)
    N %= 6

if min_pack < min_nonpack * N:
    cnt1 += min_pack
else:
    cnt1 += min_nonpack * N

cnt2 = min_nonpack * n

print(min(cnt1, cnt2))
    

