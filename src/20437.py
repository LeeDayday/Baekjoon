# 문자열 게임 2
# https://www.acmicpc.net/problem/20437
# 문자열, 슬라이딩 윈도우

# =======================================
import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

# Counter data에 특정 문자가 k개 이상 있는지 검사
def check_k(data, k):
    # flag 가 True인 경우, 정확히 k개 일 때에만 True 반환
    for key, value in data.items():
        if value >= k:
            return True
    return False

# data: 문자 별 인덱스 리스트
def solution(data, k):
    answer = [len(w), 0]
    for key, index_list in data.items():
        if len(index_list) < k:
            continue
        start, end = 0, k - 1
        while end < len(index_list):
            answer[0] = min(answer[0], index_list[end] - index_list[start] + 1)
            answer[1] = max(answer[1], index_list[end] - index_list[start] + 1)
            start += 1
            end += 1
    return answer

def get_index_data(w, data):
    for i in range(len(w)):
        data[w[i]].append(i)
    
for _ in range(int(input())): # 게임을 t회 진행
    w = list(input().rstrip()) # 알파벳 소문자로 이루어진 문자열
    k = int(input()) # 양의 정수

    if k == 1:
        print(1, 1)
        continue

    if check_k(Counter(w), k):
        index_data = defaultdict(list)
        get_index_data(w, index_data)
        print(*solution(index_data, k))

    else:
        print(-1)