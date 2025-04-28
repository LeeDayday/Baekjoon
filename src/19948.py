# 음유시인 영재
# https://www.acmicpc.net/problem/19948
# 구현, 문자열

# =======================================
import sys
from collections import Counter
input = sys.stdin.readline

data = list(input().rstrip().split()) # 시의 내용
space_cnt = int(input()) # 스페이스 바의 남은 사용 횟수
alp_cnt = list(map(int, input().split())) # 알파벳 별 남은 사용 횟수

def solution():
    # 스페이스 바의 남은 사용 횟수가 부족한 경우
    if len(data) - 1 > space_cnt:
        return -1
    
    # 알파벳 별 남은 사용 횟수 (key: 소문자 알파벳, value: 남은 횟수)
    current_counter = Counter()
    for i in range(len(alp_cnt)):
        current_counter[chr(ord('a') + i)] += alp_cnt[i]
    
    answer = ''
    for word in data:
        prev_ch = ''
        for ch in word:
            if prev_ch != ch:
                ch = ch.lower()
                # 시의 내용 작성 중 알파벳의 남은 사용 횟수가 부족한 경우
                if current_counter[ch] - 1 < 0:
                    return -1
                current_counter[ch] -= 1
                prev_ch = ch
        # 시의 제목 작성 중 알파벳의 남은 사용 횟수가 부족한 경우
        if current_counter[word[0].lower()] - 1 < 0:
            return -1

        answer += word[0].upper()
        current_counter[word[0].lower()] -= 1
        
            
    return answer

print(solution())