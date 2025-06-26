# 단축키 지정
# https://www.acmicpc.net/problem/1283
# 구현, 문자열

# =======================================
import sys
input = sys.stdin.readline

n = int(input())
commands = set()

for _ in range(n):
    cmd = input().rstrip()
    flag = False # 단축키 지정 여부
    x, y = 0, 0
    # 단어 첫글자 확인
    cmd_tokens = list(cmd.split(' '))
    for i in range(len(cmd_tokens)):
        if cmd_tokens[i][0].lower() not in commands:
            commands.add(cmd_tokens[i][0].lower())
            flag = True
            x = i
            y = 0
            break
    
    # 왼쪽에서부터 단어 알파벳 확인
    if not flag:
        for i in range(len(cmd_tokens)):
            if flag:
                break
            for j in range(len(cmd_tokens[i])):
                if cmd_tokens[i][j].lower() not in commands:
                    commands.add(cmd_tokens[i][j].lower())
                    flag = True
                    x = i
                    y = j
                    break

    # 단축키가 있는 경우, 괄호를 씌워 출력
    if flag:
        for i in range(len(cmd_tokens)):
            if i == x:
                print(f"{cmd_tokens[x][:y]}[{cmd_tokens[x][y]}]{cmd_tokens[x][y+1:]}", end=' ')
            else:
                print(cmd_tokens[i], end=' ')
        print()
    else:
        print(cmd)