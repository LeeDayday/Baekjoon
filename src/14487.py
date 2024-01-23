# 욱제는 효도쟁이야!
# https://www.acmicpc.net/problem/14487
# 구현, 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    costs = list(map(int, input().split()))
    print(sum(costs) - max(costs))