# 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662
# 자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐

# =======================================
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())

        # maxHeap, minHeap 따로 관리
        max_heap = []
        min_heap = []

        # 같은 요소에 대해 maxHeap, minHeap 모두 삭제가 이뤄져야 하므로,
        # visited: i번째 요소에 대한 pop 여부를 저장한다
        visited = [False for _ in range(k)]

        for i in range(k):
            cmd = input().split()
            if cmd[0] == 'I':
                n = int(cmd[1])
                heappush(min_heap, (n, i))
                heappush(max_heap, (-n, i))
                visited[i] = True
            elif cmd[0] == 'D':
                if cmd[1] == '1': # 최댓값 삭제
                    try:
                        # max_heap 값 정리
                        # (min_heap에서 제거되었지만, max_heap에서 제거되지 못한 값들을 제거한다)
                        while max_heap and (visited[max_heap[0][1]] is False):
                            heappop(max_heap)
                        # max_heap이 비어있지 않다면, 마지막으로 최댓값을 제거하며
                        # visited 에 pop 되었음을 표시
                        if max_heap:
                            n, i = heappop(max_heap)
                            visited[i] = False
                    except: pass

                elif cmd[1] == '-1': # 최솟값 삭제
                    try: 
                        # min_heap 값 정리
                        # (max_heap에서 제거되었지만, min_heap에서 제거되지 못한 값들을 제거한다)
                        while min_heap and (visited[min_heap[0][1]] is False):
                            heappop(min_heap)
                        # max_heap이 비어있지 않다면, 마지막으로 최댓값을 제거하며
                        # visited 에 pop 되었음을 표시
                        if max_heap:
                            n, i = heappop(min_heap)
                            visited[i] = False                    
                    except: pass

        # heap 최종 정리
        while max_heap and (visited[max_heap[0][1]] is False):
            heappop(max_heap)
        while min_heap and (visited[min_heap[0][1]] is False):
            heappop(min_heap)

        # 최댓값, 최솟값이 존재하는 경우, 해당 값 출력
        if max_heap and min_heap:
            print(-max_heap[0][0], min_heap[0][0])
        else:
            print("EMPTY")
