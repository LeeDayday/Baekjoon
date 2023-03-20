# 설탕 배달
# https://www.acmicpc.net/problem/2839
# 수학, 다이나믹 프로그래밍, 그리디

# =======================================
cnt = 0

n = int(input())

while n != 0:
    if n < 3:
        cnt = -1
        break

    if n % 5 == 0:
        cnt += n // 5
        break

    n -= 3
    cnt += 1


print(cnt)

