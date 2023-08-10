# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659
# 누적 합

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

sum_arr = [0] * n # 누적 합을 저장하는 배열
sum_arr[0] = arr[0]
for i in range(1, n):
    sum_arr[i] = sum_arr[i-1] + arr[i]
    
for _ in range(m):
    cnt = 0
    i, j = map(int, input().split())
    
    if i >= 2: 
        print(sum_arr[j-1] - sum_arr[i-2])
    else: 
        print(sum_arr[j-1])