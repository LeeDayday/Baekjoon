# 로마 숫자 재배치
# https://www.acmicpc.net/problem/2915
# 

# =======================================
import sys
import re
from itertools import permutations

input = sys.stdin.readline

# 1~9
num_dict_1 = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9
}

# 10~90
num_dict_10 = {
    'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90
}

# 정규표현식: 100 미만 로마 숫자
roman_pattern = re.compile(r'^(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$')

def is_valid(roman):
    return roman_pattern.match(roman) is not None

def rnum_to_num(rnum):
    if rnum in num_dict_1:
        return num_dict_1[rnum]
    elif rnum in num_dict_10:
        return num_dict_10[rnum]
    
    for i in range(1, len(rnum)):
        if rnum[:i] in num_dict_10 and rnum[i:] in num_dict_1:
            return num_dict_10[rnum[:i]] + num_dict_1[rnum[i:]]
    return False

# 입력 받기
original = input().strip()

min_val = float('inf')
min_roman = None

# 모든 문자 재배치 확인
for p in set(permutations(original)):
    candidate = ''.join(p)
    if is_valid(candidate):
        val = rnum_to_num(candidate)
        if val < min_val:
            min_val = val
            min_roman = candidate

print(min_roman)
