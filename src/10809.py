# 알파벳 찾기
# https://www.acmicpc.net/problem/10809
# 구현, 문자열

# =======================================
import sys
from string import ascii_lowercase
input = sys.stdin.readline

s = input().rstrip()

index_list = [-1]*26
for i in range(len(s)):
    index = ord(s[i]) - ord('a')
    if index_list[index] == -1:
        index_list[index] = i

print(*index_list)
