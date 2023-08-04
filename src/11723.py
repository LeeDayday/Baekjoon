# 집합
# https://www.acmicpc.net/problem/11723
# 구현, 비트마스킹

# =======================================
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    s = set()
    all_s = {str(i) for i in range(1, 21)}
    for _ in range(n):
        cmd = list(input().split())
        if cmd[0] == 'add':
            s.add(cmd[1])
        elif cmd[0] == 'remove':
            try: s.remove(cmd[1])
            except: pass
        elif cmd[0] == 'check':
            if cmd[1] in s:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'toggle':
            if cmd[1] in s:
                s.remove(cmd[1])
            else:
                s.add(cmd[1])
        elif cmd[0] == 'all':
            s = all_s
        elif cmd[0] == 'empty':
            s.clear()