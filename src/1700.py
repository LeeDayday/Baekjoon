# 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700
# 그리디 알고리즘

# =======================================
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

result = 0 # 코드 뽑은 횟수
plug = set() # 현재 연결된 전기용품

# idx번째 index 이후, 가장 늦게 사용되거나 더 이상 사용되지 않는 플러그 찾기
def find_last_plug(idx):
    result = 0
    max_idx = -1
    for num in plug:
        try:
            num_idx = data[idx:].index(num) # 현재 연결된 플러그가 나중에 다시 사용되는 경우
        except: # 현재 연결된 플러그가 더 이상 사용되지 않는 경우
            return num
        if max_idx < num_idx: # 가장 늦게 사용되는 플러그 찾기
            result, max_idx = num, num_idx
    return result

for i, num in enumerate(data):
    if num in plug:   
        continue

    if len(plug) >= n: # 플러그를 뽑아야하는 경우
        result += 1
        last_num = find_last_plug(i)
        plug.discard(last_num)

    plug.add(num)

print(result)
