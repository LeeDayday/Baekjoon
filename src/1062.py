# 가르침
# https://www.acmicpc.net/problem/1062
# 브루트포스 알고리즘, 비트마스킹, 백트래킹

# =======================================
import sys
from itertools import combinations
input = sys.stdin.readline


def word_to_bit(word):
    bit = 0
    for ch in word:
        bit = bit | (1 << ord(ch) - ord('a'))
    return bit

n, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(input().rstrip())

if k < 5:
    print(0)
    exit(0)
elif k >= 26:
    print(n)
    exit(0)


bits = list(map(word_to_bit, data)) # 전체 단어를 비트로 치환
base_bits = word_to_bit('antic') # 기본 알파벳: a, n, t, i, c (5개)

# 기본 알파벳을 제외한 알파벳만 포함
alphabet = [1 << i for i in range(26) if not (base_bits & 1 << i)]
result = 0
for comb in combinations(alphabet, k - 5):
    learnable_bits = sum(comb) | base_bits # 기본 알파벳 포함하여 배울 수 있는 알파벳
    cnt = 0
    for bit in bits:
        if bit & learnable_bits == bit:
            cnt += 1
    result = max(result, cnt)
print(result)