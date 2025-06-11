# 비슷한 단어
# https://www.acmicpc.net/problem/2607
# 구현, 문자열

# =======================================
import sys
from collections import Counter
input = sys.stdin.readline


n = int(input())
answer = 0
data = []

for _ in range(n):
    data.append(input().rstrip())

target = Counter(data[0])
for i in range(1, n):
    word = Counter(data[i])

    a = target - word
    b = word - target
    
    diff_a = sum(a.values())
    diff_b = sum(b.values())

    # 단어 구성이 같은 경우
    if diff_a == 0 and diff_b == 0:
        answer += 1
        print()
    # 알파벳 하나만 다른 경우
    elif diff_a * diff_b == 0 and diff_a + diff_b == 1:
        answer += 1
    elif diff_a == 1 and diff_b == 1:
        answer += 1
    

print(answer)