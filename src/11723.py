# 집합
# https://www.acmicpc.net/problem/11723
# 구현, 비트마스킹

# =======================================
import sys
from copy import deepcopy
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    s = 0
    all_s = {str(i) for i in range(1, 21)}
    for _ in range(n):
        cmd = list(input().split())
        if cmd[0] == 'add':
            s |= (1 << int(cmd[1])) # x번째 비트만 1로 만든다
        elif cmd[0] == 'remove':
            s &= ~(1 << int(cmd[1])) # x번째 비트만 0으로 만든다
        elif cmd[0] == 'check':
            # 있으면 1출력
            print(1 if s & (1 << int(cmd[1])) != 0 else 0)
        elif cmd[0] == 'toggle':
            s ^= (1 << int(cmd[1])) # x번째 비트만 toggle
        elif cmd[0] == 'all':
            s = (1<<21)-1
        elif cmd[0] == 'empty':
            s = 0