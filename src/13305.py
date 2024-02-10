# 주유소
# https://www.acmicpc.net/problem/13305
# 

# =======================================
import sys
input = sys.stdin.readline


def get_min_cost(dis, costs, n):
    # 현재 주유소보다 저렴한 주유소가 있을 때까지
    idx = 0
    total = 0
    while idx < n:
        curr_idx = idx
        while idx < n and costs[curr_idx] <= costs[idx]:
               idx += 1
        total += sum(dis[curr_idx:idx]) * costs[curr_idx]
    return total
           
            
if __name__ == '__main__':
     n = int(input())
     dis = list(map(int, input().split()))
     costs = list(map(int, input().split()))

     print(get_min_cost(dis, costs, n))
