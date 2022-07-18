import sys
from collections import deque

sys.stdin = open('input', 'r')

n, m = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0


def cheese():
    global ans

    q = deque()
    visited = [[0] * m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m : # 범위 내에 있고,
                if visited[nx][ny] == 0: # 방문한적 없다면

                    if pan[nx][ny] >= 1: # 외부공기의 인접칸이 치즈라면
                        pan[nx][ny] += 1 # 해당 치즈의 인덱스를 +1 해준다.
                    elif pan[nx][ny] == 0: # 만약 외부공기라면
                        q.append((nx, ny)) # 방문한다.
                        visited[nx][ny] = 1

    ans += 1


while True:
    flag = False
    cheese()
    for i in range(n):
        for j in range(m):
            if pan[i][j] >= 3: # 2면 이상 접촉한 경우
                pan[i][j] = 0 # 녹여준다.
                flag = True # flag 세운다.
            elif pan[i][j] == 2: # 한면만 접촉한 경우
                pan[i][j] = 1 # 다시 그냥 치즈로 업데이트

    if not flag:
        print(ans -1) # 더이상 녹일 치즈가 없어도 위의 cheese 함수가 실행되면서 ans가 +1 되기 때문에 -1해준 후 출력한다.
        break


    # for i in pan:
    #     print(i)
    #     if 1 in pan:
    #         break
    # else:
    #     print(ans)
    #     break
