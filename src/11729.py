# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729
# 재귀

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
answer = [] # 수행 과정

# 원판 개수, 시작 기둥, 목표 기둥, 보조 기둥
def hanoi(n, start, end, extra):
    if n == 1:
        answer.append([start, end])
        return
    # n - 1개를 보조 기둥으로 옮기기
    hanoi(n - 1, start, extra, end)
    # n 번째 원반을 목표 기둥으로 옮기기
    answer.append([start, end])
    # n - 1개를 다시 목표 기둥으로 옮기기
    hanoi(n - 1, extra, end, start)

    
hanoi(n, 1, 3, 2)

print(len(answer))

for result in answer:
    print(result[0], result[1])


