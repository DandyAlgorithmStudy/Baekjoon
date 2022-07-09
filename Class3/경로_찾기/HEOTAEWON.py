import sys
from collections import deque

sys.stdin = open('input', 'r')

n = int(input())
pan_input = [list(map(int, input().split())) for _ in range(n)]
pan_ans = [[0] * n for _ in range(n)]


def bfs(x, y, pan_input):
    # 최초 좌표 추가
    q = deque()
    q.append(x)
    visited = []

    while q:
        i = q.popleft() # 좌표를 입력 받음(출발지점)

        for k in range(n): # 갈 수 있는지 탐색
            if k in visited: # 방문한적 있다면 굳이 볼 필요없음
                continue
            else: # 방문한적 없다면
                if pan_input[i][k] == 1:  # i에서 k로 갈 수 있다면
                    if k == y:  # 만약 k가 목적지 y라면
                        pan_ans[x][y] = 1  # 갈수 있음 체크 후 함수 종료
                        return
                    else: # 이동할 수 있지만 아직 목적지가 아닌 경우
                        q.append(k) # queue에 추가하고
                        visited.append(k) # visited에 기록


for i in range(n):
    for j in range(n):
        if pan_input[i][j] == 1:
            pan_ans[i][j] = 1


for i in range(n):
    for j in range(n):
        if pan_ans[i][j] == 1:
            continue
        else:
            bfs(i, j, pan_ans)

for i in pan_ans:
    for j in i:
        print(j, end=' ')
    print()
