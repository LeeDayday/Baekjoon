# 센서
# https://www.acmicpc.net/problem/2212
# 그리디 알고리즘, 정렬

# =======================================
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().split()))

if k >= n:
    print(0)
    sys.exit()
    
sensors.sort()
diff = []
cnt = 0
for i in range(1, n):
    diff.append(sensors[i] - sensors[i-1])

diff.sort(reverse=True)
for i in range(k-1):
    diff.pop(0)
print(sum(diff))