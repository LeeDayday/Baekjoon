# 7 더하기
# https://www.acmicpc.net/problem/4900
# 구현, 문자열

# =======================================
import sys
from collections import defaultdict
# 7bit 이진수로 숫자 표현
dec_to_bin = {
    0: '0111111',
    1: '0001010',
    2: '1011101',
    3: '1001111',
    4: '1101010',
    5: '1100111',
    6: '1110111',
    7: '0001011',
    8: '1111111',
    9: '1101011'
}

code_to_dec = defaultdict()
dec_to_code = defaultdict()

def get_code(num):
    result = ['0', '0', '0']
    for i in range(2, -1, -1):
        if num == 0:
            break
        result[i] = str(num % 10)
        num //= 10
    return "".join(result)

def get_number(code_str):
    result = 0
    for i in range(0, len(code_str), 3):
        result *= 10
        result += code_to_dec[code_str[i:i+3]]
    return result

for key in dec_to_bin.keys():
    # 7 bit 이진수 -> 십진수
    dec = int(dec_to_bin[key], 2)
    # 십진수 -> 3자리 십진수 코드
    code_to_dec[get_code(dec)] = key

for key, value in code_to_dec.items():
    dec_to_code[value] = key

for data in sys.stdin:
    data = data.rstrip()
    if data == 'BYE':
        break
    a, b = data[:-1].split("+")
    result = get_number(a) + get_number(b)
    
    answer = ''
    for num in str(result):
        answer += dec_to_code[int(num)]
    print(data+answer)
