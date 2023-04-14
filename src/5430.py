# AC
# https://www.acmicpc.net/problem/5430
# 구현, 자료 구조, 문자열, 파싱, 덱

# =======================================
from collections import deque
import sys

T = int(sys.stdin.readline())

for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    try:
        deque = deque(arr)
    except:
        deque.extend(arr)
    flag = 0
    cnt = 0
    for cmd in p:
        if cmd == 'R':
            cnt += 1 # reverse() 는 O(n)이 걸리는 작업이니 R의 총 개수가 홀수인 경우에만 실행
        elif cmd == 'D':
            if n == 0:
                print("error")
                flag = 1
                break
            try:
                if cnt % 2:
                    deque.pop() # R이 홀수 개이면 reverse 되었다고 가정하여 오른쪽에서 pop
                else:
                    deque.popleft()
            except:
                print("error")
                flag = 1
                break
    if cnt % 2:
        deque.reverse()
    if flag == 0:
        print("[" + ",".join(deque) + "]")
    deque.clear()
