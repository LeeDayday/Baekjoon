# 전자레인지
# https://www.acmicpc.net/problem/10162
# 수학, 구현, 그리디

# =======================================
btns = [300, 60, 10]
cnt = [0]*3
idx = 0

n = int(input())

while n != 0:
    if n < 10:
        idx = -1
        break;
    else:
        cnt[idx] += n // btns[idx]
        n %= btns[idx]
        idx += 1

if idx != -1:
    for i in cnt:
        print(i, end=' ')
else:
    print(-1)
