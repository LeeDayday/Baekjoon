# 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213
# 구현, 그리디 알고리즘, 문자열

# =======================================
import string
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    alphabet_dict = {char:0 for char in string.ascii_uppercase}

    text = input().rstrip()
    len_ = len(text)

    # 이름 속에 들어있는 알파벳 개수 구하기
    for char in text:
        if char in alphabet_dict:
            alphabet_dict[char] += 1

    # 홀수 개인 알파벳 개수 구하기
    cnt = 0
    for key, value in alphabet_dict.items():
        if value % 2:
            cnt += 1
            pivot = key # 대칭 기준점
        # 홀수 개가 1개보다 많은 경우 팰린드롬 불가능
        if cnt > 1:
            print("I'm Sorry Hansoo")
            sys.exit(0)
    
    result = ''
    for key, value in alphabet_dict.items():
        result += key * (value // 2) 
    
    if len_ % 2 == 1:
        print(result + pivot + result[::-1])
    else:
        print(result + result[::-1])
    
        
    