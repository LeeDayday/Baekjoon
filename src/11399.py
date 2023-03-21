# ATM
# https://www.acmicpc.net/problem/11399
# 그리디, 정렬

# =======================================
n = int(input())
p = list(map(int, input().split()))
cnt = 0
waiting_cnt = [0] * len(p)

p.sort()

for i in range(len(p)):
  for j in range(i+1, len(p)):
    waiting_cnt[j] += p[i]

print(sum(p) + sum(waiting_cnt))