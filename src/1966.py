# 프린터 큐
# https://www.acmicpc.net/problem/1966
# 구현, 자료 구조, 시뮬레이션, 큐

# =======================================
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

# 2차원 리스트의 0번 column 최댓값 구하기
def find_max():
    queue_max = 0
    for i in range(len(queue)):
        queue_max = max(queue[i][0], queue_max)
    return queue_max

# 궁금한 문서의 출력 순서 구하기
def find_order():
    cnt = 0
    while True:
        # 0번째 문서보다 중요한 문서가 뒤에 있다면
        if queue[0][0] < find_max():
            # 0번째 문서를 맨 뒤로 배치
            queue.append(queue.pop(0))
        # 없으면, 그냥 출력 (pop)
        else:
            tmp = queue.pop(0)
            cnt += 1

        # 최근에 출력한 문서가 궁금한 문서인 경우
        if cnt > 0 and tmp[1] == file:
            # 출력 순서 print
            print(cnt)
            return
if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, file = map(int, input().split())
        priority = tuple(map(int, input().split()))

        queue = []
        for idx, p in enumerate(priority):
            queue.append((p, idx))

        find_order()