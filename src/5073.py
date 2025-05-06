# 삼각형과 세 변
# https://www.acmicpc.net/problem/5073
# 수학, 구현, 기하학

# =======================================
import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    if sum(data) == 0:
        break
    data.sort()
    if data[0] + data[1] <= data[2]:
        print("Invalid")
    elif data[0] == data[1] == data[2]:
        print("Equilateral")
    elif data[0] != data[1] != data[2]:
        print("Scalene")
    else:
        print("Isosceles")