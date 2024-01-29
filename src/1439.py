# 뒤집기
# https://www.acmicpc.net/problem/1439
# 그리디 알고리즘, 문자열

# =======================================
import sys
input = sys.stdin.readline


def get_min(s):
    # 연속된 숫자 덩어리의 개수
    cnt_0 = 0
    cnt_1 = 0
    tmp = s[0]

    for idx in range(1, len(s)):
        if s[idx] == '0':
            if s[idx] != tmp:
                cnt_1 += 1
                tmp = s[idx]
        else:
            if s[idx] != tmp:
                cnt_0 += 1
                tmp = s[idx]

    # 마지막 원소가 해당하는 집합 cnt + 1
    if s[-1] == '0':
        cnt_0 += 1
    else:
        cnt_1 += 1
    return min(cnt_0, cnt_1)

if __name__ == '__main__':
    s = input().rstrip()
    print(get_min(s))