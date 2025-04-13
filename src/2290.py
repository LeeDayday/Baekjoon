# LCD Test
# https://www.acmicpc.net/problem/2290
# 구현, 문자열

# =======================================
import sys
input = sys.stdin.readline

s, n = input().split()

s = int(s)
x = s + 2 # 가로
y = 2 * s + 3 # 세로
graph = [[' '] * ((x + 1) * len(n) - 1) for _ in range(y)]

# segment 위치별 index 정보 ([start_i][start_j], [end_i][end_j])
# segment index
#   -- a --
#  |       |
#  f       b
#  |       |
#   -- g --
#  |       |
#  e       c
#  |       |
#   -- d --

row_positions = {
    'a': ((0, 1), (0, x - 2)),
    'd': ((y - 1, 1), (y - 1, x - 2)),
    'g': ((y // 2, 1), (y // 2, x - 2))
   }
col_positions = {
     'b': ((1, x - 1), (y // 2 - 1, x - 1)),
     'c': ((y // 2 + 1, x - 1), (y - 2, x - 1)),
     'e': ((y // 2 + 1, 0), (y - 2, 0)),
     'f': ((1, 0), (y // 2 - 1, 0))
}
data = {
    '0': 'abcdef',
    '1': 'bc',
    '2': 'abged',
    '3': 'abgcd',
    '4': 'bcfg',
    '5': 'afgcd',
    '6': 'afgecd',
    '7': 'abc',
    '8': 'abcdefg',
    '9': 'abcdfg'
}

for idx, num in enumerate(n):
    cmd = data[num]

    offset = idx * (x + 1)
    for ch in cmd:
        if ch in row_positions:
            start_i, start_j = row_positions[ch][0]
            _, end_j = row_positions[ch][1]
            for j in range(start_j + offset, end_j + offset + 1):
                graph[start_i][j] = '-'
        else:
            start_i, start_j = col_positions[ch][0]
            end_i, _ = col_positions[ch][1]
            for i in range(start_i, end_i + 1):
                graph[i][start_j + offset] = '|'
    
# 출력
for row in graph:
    print(''.join(row))

