# 배
# https://www.acmicpc.net/problem/1092
# 그리디 알고리즘, 정렬

# =======================================
N = int(input())
weights = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

weights.sort(reverse=True)
boxes.sort(reverse=True)

box_idx = 0
cnt = 0

if weights[0] < boxes[0]:
    print(-1)

else:
    while boxes:
        if not boxes: # boxes 가 모두 비었다면 break
            break

        for weight in weights:
            for box in boxes:
                if weight >= box:
                    boxes.remove(box)
                    break
        cnt += 1
    
    print(cnt)