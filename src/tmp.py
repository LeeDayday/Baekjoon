# 복습 - 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659

# O(N)

import sys
input = sys.stdin.readline

vowels = {'a', 'e', 'i', 'o', 'u'}

def check_password(data):
    flag_v = False
    for i in range(len(data)):
        if data[i] in vowels:
            flag_v = True
        if i > 0 and data[i] == data[i - 1]:
            # 'ee' 'oo' 외 두 문자가 연속한 경우 false
            if data[i] != 'e' and data[i] != 'o':
                return False
    # 모음이 없는 경우, false
    if flag_v is False:
        return False
    
    # 자음/모음이 3번 연속되는 경우 false
    cnt = [0, 0] # 연속적인 (자음, 모음) 개수
    if len(data) >= 3:
        for i in range(len(data)):
            if cnt[0] == 3 or cnt[1] == 3:
                return False
            if data[i] in vowels:
                cnt[1] += 1
                cnt[0] = 0
            else:
                cnt[0] += 1
                cnt[1] = 0
    if cnt[0] == 3 or cnt[1] == 3:
        return False
    return True
while True:
    data = input().rstrip()
    if data == 'end':
        break
    if check_password(data):
        print(f"<{data}> is acceptable.")
    else:
        print(f"<{data}> is not acceptable.")