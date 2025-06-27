# 문자열 교환
# https://www.acmicpc.net/problem/1522
# 

# =======================================
import sys
input = sys.stdin.readline

data = input().rstrip()
cnt_a = data.count('a') # a의 개수
data += data[0:cnt_a - 1] # 원형 문자열을 표현하기 위해 문자열 확장

answer = float('inf')
for i in range(len(data) - cnt_a + 1):
    answer = min(answer, data[i:i+cnt_a].count('b'))
print(answer)