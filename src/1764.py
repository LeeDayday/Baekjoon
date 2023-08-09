# 듣보잡
# https://www.acmicpc.net/problem/1764
# 

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

never_heard = set()
for _ in range(n):
    never_heard.add(input().rstrip())

never_seen = set()
for _ in range(m):
    never_seen.add(input().rstrip())

never_heard_and_seen = list(never_heard.intersection(never_seen))
never_heard_and_seen.sort()
print(len(never_heard_and_seen))
for i in range(len(never_heard_and_seen)):
    print(never_heard_and_seen[i])