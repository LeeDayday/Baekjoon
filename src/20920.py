# 영단어 암기는 괴로워
# https://www.acmicpc.net/problem/20920
# 자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 집합과 맵

# =======================================
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
data = defaultdict(int)

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        data[word] += 1

answer = []
for word, cnt in data.items():
    answer.append((cnt, len(word), word))
    
answer.sort(key=lambda x: (-x[0], -x[1], x[2]))

for i in range(len(answer)):
    print(answer[i][2])