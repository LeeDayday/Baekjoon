# 동전 0
# https://www.acmicpc.net/problem/11047
# 

# =======================================
n, k = map(int, input().split())
A = []
cnt = 0
idx = 0
for i in range(n):
    A.append(int(input()))

A.sort(reverse=True)

while k != 0:
    print(cnt, n, idx)
    if idx >= n:
        break
    cnt += k // A[idx]
    k %= A[idx]
    idx += 1

print(cnt)