# 계단 오르기
# https://www.acmicpc.net/problem/2579
# 

# =======================================
import sys
input = sys.stdin.readline

n = int(input())

scores = []
for _ in range(n):
    scores.append(int(input()))

# dp에는 각 계단 도달 시 점수의 최댓값을 저장한다
dp = [0 for _ in range(n)]

# 문제 접근 방법
# 1. 최대한 1 계단씩 올라야 총 점수가 최대가 된다
# 2. 3연속 1계단은 불가능.
# 3. 마지막 계단은 반드시 밟아야 함

# 한 계단 올라 도달한 경우, 두 계단 올라 도달한 경우
dp[0] = scores[0]

if n > 1: # index Error 방지 위해 경우 나눠서
    dp[1] = scores[0] + scores[1]
    
# 세번째 계단부터 점화식 적용
for i in range(2, n):
    # i번째 계단은 (2+1) 혹은 (2) 의 조합으로 도달한다.
    # 즉, i번째 계단을 1+1의 조합으로 도달하지 않는다는 뜻 (위에 명시한 조건 2, 3을 만족하기 위하여)
    dp[i] = max(dp[i-3]+ scores[i-1]+scores[i], dp[i-2]+scores[i])


print(dp[-1])