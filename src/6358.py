# Four Quarters
# https://www.acmicpc.net/problem/6358
# 

# =======================================
from collections import defaultdict

# player A, B의 경우의 수에 대한 점수표
payoff_a = [[1, 1, 2], [0, 0, 1], [-1, 0, 0]]
payoff_b = [[0, -1, -1], [1, 0, 0], [2, 0, -1]]

# 각 경우가 나올 확률 (HH), (HT), (TT)
prob = [
    [0.25 * 0.25, 0.25 * 0.5, 0.25 * 0.25],
    [0.5 * 0.25,  0.5 * 0.5,  0.5 * 0.25],
    [0.25 * 0.25, 0.25 * 0.5, 0.25 * 0.25]
]

state = defaultdict(float) # key: 점수 차이 (A-B), value: 해당 점수 차이가 발생할 확률
state[0] = 1.0  # 초기 점수 차: 0, 확률: 1

print("Round   A wins    B wins    Tie")
for rnd in range(1, 21): # 총 20라운드
    new_state = defaultdict(float)
    for diff, p in state.items(): # 이전에 발생했던 경우(발생한 점수 차) 및 확률에 이어서 진행
        for i in range(3):
            for j in range(3):
                # 경우 [i][j] 에 대해 A, B가 받는 점수: a, b
                a = payoff_a[i][j] 
                b = payoff_b[i][j]
                score_diff = diff + (a - b)
                new_state[score_diff] += p * prob[i][j]
    # 발생한 점수 차 기록 업데이트
    state = new_state
    # i 번째 라운드에서 a가 이길 확률, b가 이길 확률, 비길 확률
    a_win = 0
    b_win = 0
    tie = 0
    for diff, p in state.items():
        if diff > 0:
            a_win += p
        elif diff < 0:
            b_win += p
        else:
            tie += p
    print(f"{rnd:5}   {a_win:8.4%}  {b_win:8.4%}  {tie:8.4%}")

