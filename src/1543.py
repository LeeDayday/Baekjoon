# 문서 검색
# https://www.acmicpc.net/problem/1543
# 문자열, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

file = input().rstrip()
word = input().rstrip()

word_len = len(word)
cnt = 0
i = 0
while True:
    if i >= len(file):
        break
    if file[i:i+word_len] == word:
        cnt += 1
        i += word_len
    else:
        i += 1    

print(cnt)
