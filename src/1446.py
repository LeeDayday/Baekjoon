# 지름길
# https://www.acmicpc.net/problem/1446
# 다이나믹 프로그래밍, 그래프 이론, 최단 경로, 데이크스트라

# =======================================
import sys
input = sys.stdin.readline

n, d = map(int, input().split()) # n: 지름길 개수, d: 고속도로 길이

data = []
for _ in range(n):
    data.append(list(map(int, input().split()))) # 지름길 시작 위치, 도착 위치, 길이

data.sort()

# dp[i]: i 위치 도달하기까지 거리 최솟값
dp = [i for i in range(d + 1)]


# 지름길을 이용하는 경우 고려
for start, end, dist in data:
    if end > d:
        continue
    for j in range(1, d + 1):
        if end == j:
            # 지름길 유무 판단
            dp[j] = min(dp[j], dp[start] + dist)
        else:
            # dp 업데이트
            dp[j] = min(dp[j], dp[j - 1] + 1)

print(dp[-1])

