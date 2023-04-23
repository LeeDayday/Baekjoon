# 주식
# https://www.acmicpc.net/problem/11501
# 그리디

# =======================================
import sys

def find_max_profit(price_list, days):
    idx = days - 1 # 뒤에서부터 훑는다
    i = idx -1
    cnt = 0
    while idx > 0:
        if i == -1:
            break
        if price_list[i] >= price_list[idx]:
            idx -= 1
            i = idx - 1
            continue
        cnt += price_list[idx] - price_list[i]
        price_list[i] = 0
        i -= 1
    return cnt
    
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    print(find_max_profit(arr, n))
