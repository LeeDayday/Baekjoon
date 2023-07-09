# 종이 접기
# https://www.acmicpc.net/problem/1802
# 애드 혹, 분할 정복

# =======================================
import sys
input = sys.stdin.readline

t = int(input())

def is_available(str):
    str_len = len(str)
    if str_len == 1:
        return True
    for i in range(str_len//2):
        if str[i] == str[str_len - 1 - i]:
            return False

    return is_available(str[:str_len//2]) and is_available(str[str_len//2+1:str_len])

for _ in range(t):
    papers = input().rstrip()

    if is_available(papers):
        print("YES")
    else:
        print("NO")
