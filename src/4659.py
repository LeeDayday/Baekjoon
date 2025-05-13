# 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659
# 구현, 문자열

# =======================================
import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

def solution(data):
    flag = False # 모음 포함 여부
    # 조건 1, 3 확인
    for i in range(len(data)):
        if data[i] in vowels:
            flag = True
        if i + 1 < len(data) and data[i] == data[i + 1]:
            if data[i] != 'e' and data[i] != 'o':
                return False
    if flag is False:
        return False
    # 조건 2 확인
    cnt = [0, 0] # 연속된 (자음, 모음) 수
    if len(data) >= 3:
        for i in range(len(data)):
            if cnt[0] == 3 or cnt[1] == 3:
                return False
            if data[i] in vowels:
                cnt[0] = 0
                cnt[1] += 1
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
    if solution(data):
        print(f"<{data}> is acceptable.")
    else:
        print(f"<{data}> is not acceptable.")

