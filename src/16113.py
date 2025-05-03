# 시그널
# https://www.acmicpc.net/problem/16113
# 구현, 문자열

# =======================================
import sys
input = sys.stdin.readline

# 열 단위로 숫자 읽기
numbers = {
    '0': ['#','#','#','#','#','#','.','.','.','#','#','#','#','#','#'],
    '1': ['#','#','#','#','#'],
    '2': ['#','.','#','#','#','#','.','#','.','#','#','#','#','.','#'],
    '3': ['#','.','#','.','#','#','.','#','.','#','#','#','#','#','#'],
    '4': ['#','#','#','.','.','.','.','#','.','.','#','#','#','#','#'],
    '5': ['#','#','#','.','#','#','.','#','.','#','#','.','#','#','#'],
    '6': ['#','#','#','#','#','#','.','#','.','#','#','.','#','#','#'],
    '7': ['#','.','.','.','.','#','.','.','.','.','#','#','#','#','#'],
    '8': ['#','#','#','#','#','#','.','#','.','#','#','#','#','#','#'],
    '9': ['#','#','#','.','#','#','.','#','.','#','#','#','#','#','#']
}

n = int(input())
data = list(input().rstrip())
step = n // 5

graph = []
for i in range(5):
    graph.append(data[i * step: i * step + step])

def get_number(result):
    for key, value in numbers.items():
        if value == result:
            return key
    
answer = ''
result = []
for y in range(step):
    tmp = []
    for x in range(5):
        tmp.append(graph[x][y])
    # 공백 열을 기준으로 숫자 구하기
    if tmp == ['.', '.', '.', '.', '.']:
        if result:
            answer += get_number(result)
            result = []
    else:
        result.extend(tmp)
# 공백 열 없이 숫자가 끝나는 경우 계산
if result:
    answer += get_number(result)

print(answer)