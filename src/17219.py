# 비밀번호 찾기
# https://www.acmicpc.net/problem/17219
# 자료 구조, 해시를 사용한 집합과 맵

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memo = {}
for _ in range(n):
    str = input().split()
    memo[str[0]] = str[1]

for _ in range(m):
    print(memo.get(input().rstrip()))