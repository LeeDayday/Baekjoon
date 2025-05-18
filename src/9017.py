# 크로스 컨트리
# https://www.acmicpc.net/problem/9017
# 구현

# =======================================
import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    team_counter = Counter(data)

    team = {num for num, cnt in team_counter.items() if cnt == 6}
    team_scores = defaultdict(list)

    score = 1
    for num in data:
        if num in team:
            team_scores[num].append(score)
            score += 1
    result = [] # (상위 4명 점수, 다섯 번째 선수 점수, 팀 번호)

    for num in team_scores:
        total = sum(team_scores[num][:4])
        fifth = team_scores[num][4]
        result.append((total, fifth, num))

    result.sort(key=lambda x: (x[0], x[1]))

    print(result[0][2])
