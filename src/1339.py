# 단어 수학
# https://www.acmicpc.net/problem/1339
# 그리디 알고리즘

# =======================================
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    alphabet_cnt = {}

    for _ in range(n):
        word = reversed(input().rstrip())
        for idx, alpha in enumerate(word):
            # dictionary에 존재하지 않은 경우
            if alpha not in alphabet_cnt:
                alphabet_cnt[alpha] = 10 ** idx
            # 이미 존재한 경우
            else:
                alphabet_cnt[alpha] += 10 ** idx
    # key - value 사이의 관계는 더 이상 중요하지 않음. value 값을 기준으로 내림차순 정렬
    alphabet_cnt = sorted(alphabet_cnt.values(), reverse=True)
    total = 0
    num = 9
    for cnt in alphabet_cnt:
        total += cnt * num
        num -= 1

    return total


if __name__ == '__main__':
    print(solution())
