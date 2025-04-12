# CPU
# https://www.acmicpc.net/problem/16506
# 구현

# =======================================
import sys
input = sys.stdin.readline

opcode = {
    'ADD': '0000',
    'SUB': '0001',
    'MOV': '0010',
    'AND': '0011',
    'OR': '0100',
    'NOT': '0101',
    'MULT': '0110',
    'LSFTL': '0111',
    'LSFTR': '1000',
    'ASFTR': '1001',
    'RL': '1010',
    'RR': '1011',
}

for _ in range(int(input())):
    cmd, x, y, z = input().split()
    x = format(int(x), '03b')
    y = format(int(y), '03b')

    result = ''
    # 0 ~ 5 bit
    if cmd[-1] == 'C':
        result += opcode[cmd[:-1]] + '10'
    else:
        result += opcode[cmd] + '00'
    # 6 ~ 8 bit
    result += x
    # 9 ~ 11 bit
    if cmd == 'NOT' or cmd[:3] == 'MOV':
        result += '000'
    else:
        result += y
    # 12 ~ 15 bit
    if cmd[-1] == 'C':
        result += format(int(z), '04b')

    else:
        result += format(int(z), '03b')
        result += '0'       

    print(result)