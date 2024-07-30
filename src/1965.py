# 상자넣기
# https://www.acmicpc.net/problem/1965
# 다이나믹 프로그래밍

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [1] * n
# i번째 상자(여러 개일 수 있음)가 j번째 상자에 들어갈 수 있는지 확인
for i in range(n):
    for j in range(i+1, n):
        if data[i] < data[j]:
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))
    