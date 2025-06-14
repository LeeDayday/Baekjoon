# 가희와 키워드
# https://www.acmicpc.net/problem/22233
# 자료 구조, 문자열, 해시를 사용한 집합과 맵, 파싱, 집합과 맵

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 메모장에 적은 키워드 개수, m: 블로그에 쓴 글의 개수

memo = set() # 메모장에 적은 키워드

for _ in range(n):
    memo.add(input().rstrip())

keyword = [] # 블로그에 쓴 글과 관련된 키워드
for _ in range(m):
    keywords = list(input().rstrip().split(','))
    for keyword in keywords:
        if keyword in memo:
            memo.remove(keyword)

    print(len(memo))
