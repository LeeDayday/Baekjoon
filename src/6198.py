# 옥상 정원 꾸미기
# https://www.acmicpc.net/problem/6198
# 자료 구조, 스택

# =======================================
import sys

n = int(sys.stdin.readline())

heights = []
for i in range(n):
    heights.append(int(sys.stdin.readline()))

stack = []
cnt = 0

# 오른쪽으로 나보다 작은 빌딩 개수 == 왼쪽으로 나보다 큰 빌딩 개수
# stack에는 height(나) 기준 왼쪽을 봤을 때 나보다 큰 애들 저장
for height in heights:
    # 나보다 큰 애가 나올 때까지 pop
    while stack and stack[-1] <= height:
        stack.pop()

    cnt += len(stack)
    stack.append(height)
    
print(cnt)

        