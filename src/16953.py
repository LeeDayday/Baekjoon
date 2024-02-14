# A -> B
# https://www.acmicpc.net/problem/16953
# 그래프 이론, 그리디 알고리즘, 그래프 탐색, 너비 우선 탐색

# =======================================
import sys
from collections import deque
input = sys.stdin.readline

def find_a_to_b(a, b):
    queue = deque()
    cnt = 0
    queue.append((a, cnt))
    while queue:
        val, cnt = queue.popleft()
        # 2를 곱한 수
        tmp = val * 2
        if tmp == b:
            return cnt + 1
        elif tmp > b: # b보다 큰 수인 경우, 더 이상 queue에 추가하지 않는다
            continue
        else:
            queue.append((tmp, cnt + 1))

        # 가장 오른쪽에 1를 추가한 수
        tmp = val * 10 + 1
        if tmp == b:
            return cnt + 1
        elif tmp > b:
            continue
        else:
            queue.append((tmp, cnt + 1))

    # b로 만들 수 없는 경우
    return -1


if __name__ == '__main__':
    a, b = map(int, input().split())

    result = find_a_to_b(a, b)
    if result == -1:
        print(result)
    else:
        print(result + 1)
