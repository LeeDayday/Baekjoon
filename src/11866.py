# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
# 구현, 자료구조, 큐

# =======================================
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
result = []
idx = 0
while True:
    # k 번째 순서 구하기
    step = 0
    while True:
        # 제거되지 않은 요소만 고려
        if arr[idx] != 0:
            step += 1
        if step == k:
            break
        # k 번째 순서에 도달할 때까지 검사
        idx = (idx + 1) % n

    result.append(arr[idx])
    # 방문 표시
    arr[idx] = 0
    # 요세푸스 순열을 모두 구한 경우 break
    if len(result) == n:
        break
    
print("<" + ", ".join(str(x) for x in result) + ">")