# KCPC
# https://www.acmicpc.net/problem/3758
# 구현, 정렬

# =======================================
import sys
from collections import defaultdict
input = sys.stdin.readline

class Team:
    def __init__(self, id, k):
        self.id = id
        self.scores = [0] * k
        self.submitted_cnt = 0
        self.last_submitted = 0
    
    def update_score(self, j, s, t):
        # 팀 id, 문제 번호, 점수, 제출 시간
        if self.scores[j] < s:
            self.scores[j] = s
        # 제출 횟수 증가
        self.submitted_cnt += 1
        # 마지막 제출 시간 갱신
        self.last_submitted = t

    def get_total_score(self):
        # [팀 번호, 최종 점수, 총 제출 횟수, 마지막 제출 시간] 반환
        return [self.id, sum(self.scores), self.submitted_cnt, self.last_submitted]
    
for _ in range(int(input())):
    n, k, t, m = map(int, input().split()) # 팀 개수, 문제 개수, 내 팀 id, 로그 엔트리 개수
    
    team_list = [Team(i, k) for i in range(1, n + 1)]
    for time in range(m):
        i, j, s = map(int, input().split())
        
        team_list[i - 1].update_score(j - 1, s, time)

    answer = []
    for i in range(n):
        answer.append(team_list[i].get_total_score())
    
    answer.sort(key=lambda x: (-x[1], x[2], x[3]))
    for i in range(n):
        if t == answer[i][0]:
            print(i + 1)
            break
