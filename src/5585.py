# 거스름돈
# https://www.acmicpc.net/problem/5585
# 그리디

# =======================================
arr = [500, 100, 50, 10, 5, 1]

n = int(input())

# 거스름돈
change = 1000 - n

cnt = 0
idx = 0

while change > 0:
    cnt += change // arr[idx] # 잔돈 개수
    change %= arr[idx]
    idx += 1

print(cnt)