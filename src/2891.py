# 카약과 강풍
# https://www.acmicpc.net/problem/2891
# 구현, 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline
# 전체 팀, 손상된 팀, 여분 팀의 수 입력
n, s, r = map(int, input().split())
# 카약이 손상된 팀 번호
damaged_list = list(map(int, input().split()))
# 여분 팀 번호
extra_list = list(map(int, input().split()))
# 출전 불가능 팀
cnt = 0

# 여분이 있으면서 손상된 경우(자기 자신에게 대여하는 경우)
intersection = (set(damaged_list) & set(extra_list))
damaged_list = list(set(damaged_list) - intersection)
extra_list = list(set(extra_list) - intersection)

# 이웃에게 빌려야 하는 경우
for damaged_team in damaged_list:
    # 여분 팀의 카약이 손상된 경우
    if damaged_team-1 in extra_list:
        extra_list.remove(damaged_team-1)
    elif damaged_team+1 in extra_list:
        extra_list.remove(damaged_team+1)
    else:
        cnt += 1

print(cnt)