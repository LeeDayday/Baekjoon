# 걷기
# https://www.acmicpc.net/problem/1459
# 수학, 많은 조건 분기

# =======================================
import sys
import math
x, y, w, s = map(int, sys.stdin.readline().split())
total = 0

# (2, 0) or (0, 2)의 최솟값
min1 = min(2*w, 2*s)

# (1, 1)의 최솟값
min2 = min(2*w, s)
if x * y == 0:
    if max(x,y) > 1:
        print(min1 * (max(x,y)//2) + w * (max(x,y)%2))
        sys.exit(0)
    else:
        if max(x, y) == 0:
            print(0)
        else:
            print(w)
        sys.exit(0)

if min1 < min2:
    # (2, 0) or (0, 2) 씩 이동
    if min(x, y) >= 2:
        total += min1 * (x // 2 + y // 2)
        x %= 2
        y %= 2

# (1, 1)씩 이동
if x * y > 0:
    min_val = min(x,y)
    total += min_val * min2
    x -= min_val
    y -= min_val
if x > 0:
    total += min1 * (x // 2) + w * (x % 2)
   
elif y > 0:
    total += min1 * (y // 2) + w * (y % 2)

print(total)