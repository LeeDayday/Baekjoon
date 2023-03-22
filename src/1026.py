# 보물
# https://www.acmicpc.net/problem/1026
# 수학, 그리디, 정렬

# =======================================
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = 0
m = max(B)
A.sort()

for i in range(len(B)):
    s += A[i] * m
    idx = B.index(m)
    B[idx] = 0
    m = max(B)

print(s)