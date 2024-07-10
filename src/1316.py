# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
# 구현, 문자열

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    data = input().rstrip()
    unique_cnt = len(set(data))

    tmp_cnt = 1
    tmp_ch = data[0]
    for ch in data:
        if tmp_ch != ch:
            tmp_cnt += 1
            tmp_ch = ch
    if tmp_cnt == unique_cnt:
        result += 1

print(result)