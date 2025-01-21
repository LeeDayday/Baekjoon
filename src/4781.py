# 사탕 가게
# https://www.acmicpc.net/problem/4781
# 다이나믹 프로그래밍, 배낭 문제

# =======================================

import sys
input = sys.stdin.readline

while True:
    n, m = input().split()
    
    if n == '0':
        break
    n = int(n)
    m = int(float(m) * 100)
    dp = [0] * (m + 1)
    data = []
    for _ in range(n):
        c, p = input().split()
        data.append([int(c) * 100, int(float(p) * 100 + 0.5)])
        
    for i in range(n):
        calory = data[i][0]
        price = data[i][1] 
        if price > m:
            continue
        for j in range(price, m + 1):
            if dp[j] < dp[j - price] + calory:
                dp[j] = dp[j - price] + calory

    print(int(dp[-1] * 0.01))