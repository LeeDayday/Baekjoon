# 피보나치 함수
# https://www.acmicpc.net/problem/1003
# 

# =======================================
import sys
input = sys.stdin.readline


def fibonacci(n):
    length_zero = len(zero)
    # 피보나치 수열로 더 표현할 수 있는 경우
    if n >= length_zero:
        for i in range(length_zero, n+1):
            # f(n) = f(n-1) + f(n-2)
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(f"{zero[n]} {one[n]}")

    
        

if __name__ == '__main__':
    t = int(input())

    # f(0) = f(0)
    # f(1) = f(1)
    # f(2) = f(1) + f(0) <- 2부터 규칙 적용
    zero = [1, 0, 1]
    one = [0, 1, 1]
    for _ in range(t):
        fibonacci(int(input()))
        

