# 간판
# https://www.acmicpc.net/problem/5534
# 문자열, 브루트포스 알고리즘

# =======================================
import sys
input = sys.stdin.readline

answer = 0

n = int(input())
target = input().rstrip()
data = []

for _ in range(n):
    data.append(input().rstrip())

for name in data:
    flag = 0
    for i in range(len(name)):
        if flag == 1:
            break
        if name[i] == target[0]:
            for j in range(i, len(name)):
                if name[j] == target[-1]:
                    turn = (j - i) // (len(target) - 1) # 간격
                    cnt = 0
                    while cnt < len(target):
                        if name[i + turn * cnt] == target[cnt]:
                            cnt += 1
                        else:
                            break
                    if cnt == len(target):
                        flag = 1
                        answer += 1
                        break


print(answer)