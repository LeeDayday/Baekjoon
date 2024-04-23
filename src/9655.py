# 돌 게임
# https://www.acmicpc.net/problem/9655
# 

# =======================================
import sys
input = sys.stdin.readline


def solution(n):
    # 상근: 2, 창영: 3
    dp = [0] * (n+1)
    if n <= 3:
        if n == 2:
            print("CY")
            return
        else:
            print("SK")
            return

    dp[1] = 2
    dp[3] = 2
    for i in range(1, n):
        if dp[i] == 2:
            if i+1 <= n and dp[i+1] == 0:
                dp[i+1] = 3
            if i+3 <= n and dp[i+3] == 0:
                dp[i+3] = 3
        elif dp[i] == 3:
            if i+1 <= n and dp[i+1] == 0:
                dp[i+1] = 2
            if i+3 <= n and dp[i+3] == 0:
                dp[i+1] = 2
    if dp[n] == 2:
        print("SK")
    else:
        print("CY")
    
if __name__ == '__main__':
    n = int(input())
    solution(n)