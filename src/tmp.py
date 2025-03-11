# 복습 - 가르침
# https://www.acmicpc.net/problem/1062

from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = []
for _ in range(n):
    words.append(input().rstrip())
    
def word_to_bit(word):
    bit = 0
    for ch in word:
        bit = bit | (1 << ord(ch) - ord('a'))
    return bit

def solution(n, k, words):
    if k < 5:
        return 0
    elif k >= 26:
        return n
    
    
    bits = list(map(word_to_bit, words)) # 입력받은 모든 단어를 비트로 변환
    base_bits = word_to_bit('antic') # 남극언어 기본 알파벳
    alphabets = [1 << i for i in range(26) if not(base_bits & 1 << i)] # 기본 알파벳을 제외한 알파벳의 비트 값만 리스트에 추가
    answer = 0
    for comb in combinations(alphabets, k - 5): # 배울 수 있는 알파벳 조합
        learnable_bits = sum(comb) | base_bits
        print(learnable_bits)
        cnt = 0
        for bit in bits:
            if bit & learnable_bits == bit:
                cnt += 1
        answer = max(answer, cnt)
            
        # learnable_bits = comb | 


    return answer

print(solution(n, k, words))


