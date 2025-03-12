# 복습 - 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n: 멀티탭 구멍 개수, k: 전기용품 사용 횟수
data = list(map(int, input().split())) # 전기 용품 사용 순서

def solution(n, k, data):
    answer = 0
    using = set() # 사용 중인 멀티탭

    for i, num in enumerate(data):
        using.add(num)
        # 플러그를 뽑아야 하는 경우
        if len(using) > n: 
            # 사용중인 플러그 중 가장 나중에 사용되거나, 사용되지 않는 플러그 제거
            last_idx = 0
            last_num = 0 # 제거할 플러그
            for using_num in using:
                try:
                    idx = data[i:].index(using_num) # using_num이 이후에 사용될 경우의 idx
                except:
                    last_num = using_num # using_num은 이후에 다시 사용되지 않음
                    break
                if last_idx < idx:
                    last_idx = idx
                    last_num = using_num
            
            using.remove(last_num)
            answer += 1

    return answer

print(solution(n, k, data))


