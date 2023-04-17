# 센서
# https://www.acmicpc.net/problem/2212
# 그리디 알고리즘, 정렬

# =======================================
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().split()))

sensors.sort()
diff = []
cnt = 0
for i in range(n-1):
    diff.append(sensors[i+1] - sensors[i])

diff.sort(reverse=True)
for i in range(k):
    diff.pop(0)
print(sum(diff))