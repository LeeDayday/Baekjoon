# 신입 사원
# https://www.acmicpc.net/problem/1946
# 그리디 알고리즘, 정렬

# =======================================
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        scores = []
        
        for _ in range(n):
            scores.append(list(map(int, input().split())))

        scores.sort(key=lambda x:(x[0], x[1]))

        least = 0 # 면접 점수 꼴등의 index (0번 index는 서류 1등이므로 무조건 합격)
        cnt = 1 # 선발 가능 인원 수
        for i in range(1, n):
            if scores[i][1] < scores[least][1]:
                least = i
                cnt += 1
        print(cnt)
        

