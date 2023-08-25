# 패션왕 신해빈
# https://www.acmicpc.net/problem/9375
# 수학, 자료구조, 조합론, 해시를 사용한 집합과 맵

# =======================================
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        clothes = {}
        for _ in range(n):
            name, genre = input().split()
            # 해당 키가 존재한다면 리스트에 추가
            if genre in clothes:
                clothes[genre].append(name)
            # 처음 딕셔너리에 추가된다면 value를 list에 담아 딕셔너리에 추가
            else:
                clothes[genre] = [name]
        cnt = 1
        # 의상 장르 별 개수        
        for k in clothes:
            cnt *= (len(clothes[k]) + 1)
        
        print(cnt-1)