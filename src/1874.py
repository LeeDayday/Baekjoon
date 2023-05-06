# 스택 수열
# https://www.acmicpc.net/problem/1874
# 자료 구조, 스택

# =======================================
import sys

def find_sequence(stack, arr, popped):
    result = []
    top = 1 # 가장 마지막으로 push한 값 (push 최댓값)
    for num in arr:
        while top <= num:
            stack.append(top)
            result.append('+')
            top += 1
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return False, result
    return True, result

n = int(sys.stdin.readline())

stack = []
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

popped = [False] * n
result = find_sequence(stack, arr, popped)

if result[0] is True:
    for i in result[1]:
        print(i)
else:
    print("NO")