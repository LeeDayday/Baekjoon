# 문자열 복사
# https://www.acmicpc.net/problem/2195
# 그리디 알고리즘, 문자열 

# =======================================
import sys
input = sys.stdin.readline

# copy(s,p) : S의 s번 문자부터 p개의 문자를 P에 복붙
s = input().rstrip()
p = input().rstrip()

result = 0
idx = 0
while idx < len(p):
    tmp = ''
    # 문자열 p가 문자열 s에 존재하는 경우
    if s.find(p[idx:]) != -1:
        result += 1
        break
    for j in range(idx, len(p)):
        tmp += p[j]
        if s.find(tmp) == -1:
            result += 1
            idx = j
            break
print(result)
