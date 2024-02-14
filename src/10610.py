# 30
# https://www.acmicpc.net/problem/10610
# 수학, 그리디 알고리즘, 문자열, 정렬, 정수론

# =======================================
import sys
input = sys.stdin.readline

def get_max(n):
    # 0이 없으면 탈락
    if n.find('0') == -1:
        return -1
    
    # 3의 배수가 아니면 탈락
    cnt = 0
    for num in n:
        cnt += int(num)

    if cnt % 3 != 0:
        return -1
    
    # 문자열을 오름차순으로
    n = list(n)
    n.sort(reverse=True)
    return ''.join(n)
    

if __name__ == '__main__':
    n = input().rstrip()
    print(get_max(n))