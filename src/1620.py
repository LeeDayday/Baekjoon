# 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620
# 자료구조, 해시를 사용한 집합과 맵

# =======================================
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_name_dogam = {} # 포켓몬 도감 (번호: 이름)

for i in range(1, n+1):
    num_name_dogam[i] = input().rstrip()

name_num_dogam = {v:k for k, v in num_name_dogam.items()} # 포켓몬 도감 (이름: 번호)
for i in range(m):
    question = input().rstrip()

    # 숫자를 입력한 경우
    try:
        print(num_name_dogam.get(int(question))) # key 로 value 얻기
    # 포켓몬 이름을 입력한 경우
    except:
        print(name_num_dogam.get(question)) # value로 key 얻기
