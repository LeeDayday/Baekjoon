# 단어 정렬
# https://www.acmicpc.net/problem/1181
# 문자열, 정렬

# =======================================
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

if __name__ == '__main__':
    
    n = int(input())

    str_list = []
    for _ in range(n):
        str_list.append(input().rstrip())

    # 중복 값 제거
    str_list = list(set(str_list))
    
    # 알파벳 순으로 정렬
    str_list.sort()
    # 길이 순으로 정렬
    str_list.sort(key=len)
    for str in str_list:
        print(str)