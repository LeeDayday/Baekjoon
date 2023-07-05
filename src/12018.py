# Yonsei TOTO
# https://www.acmicpc.net/problem/12018
# 

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

student_list = []
mileage_list = []
seongjun_mileage_list = []
cnt = 0

for _ in range(n):
    # 해당 강의의 신청한 사람 수, 수강 인원 입력
    student_list.append(list(map(int, input().split())))
    # 해당 강의의 마일리지 리스트 입력
    mileage_list.append(list(map(int, input().split())))

for i in range(n):
    # 신청 정원 < 수강 정원인 경우
    if student_list[i][0] < student_list[i][1]:
        # 최소한의 마일리지를 사용해도 수강신청 성공
        seongjun_mileage_list.append(1)
    # 신청 정원 >= 수강 정원인 경우
    else:
        # 소비한 마일리지 수가 순위 내에 들어야 함
        last_idx = student_list[i][1] - 1
        mileage_list[i].sort(reverse=True)
        seongjun_mileage_list.append(mileage_list[i][last_idx])

seongjun_mileage_list.sort()
for num in seongjun_mileage_list:
    m -= num
    if m < 0:
        break
    cnt += 1

print(cnt)