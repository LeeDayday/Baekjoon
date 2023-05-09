# 탑
# https://www.acmicpc.net/problem/2493
# 자료 구조, 스택

# =======================================
import sys

n = int(sys.stdin.readline())

sender = list(map(int, sys.stdin.readline().split()))
stack = []
receiver = []
for i in range(0, n):
    curr_info = (i+1, sender[i])
    print(f"curr_info: {curr_info}")
    while True:
        try: 
            top_info = stack.__getitem__(-1)
        except: 
            # stack이 비어있는 경우 ==> 현재 탑이 가장 높은 경우
            print("== empty stack == I am the tallest ==")
            stack.append(curr_info)
            receiver.append(0)
            print(f"stack: {stack}")
            print(f"receiver:{receiver}")
            break
        # 현재 탑보다 높은 탑이 있는 경우
        print(f"stack's top_info: {top_info}")
        if top_info[1] > curr_info[1]:
            stack.append(curr_info)
            receiver.append(top_info[0])
            print(f"== stack max exist == {top_info[1]} > {curr_info[1]}")
            print(f"stack: {stack}")
            print(f"receiver:{receiver}")
            break    
        else:
            print("pop")
            stack.pop()
        print(f"stack: {stack}")
        print(f"receiver:{receiver}")

for num in receiver:
    print(num, end=' ')   
