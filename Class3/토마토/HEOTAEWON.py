import sys
from collections import deque

sys.stdin = open('input', 'r')

m, n, h = map(int, sys.stdin.readline().split())

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

pan = []
q = deque()

for k in range(h):
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
        for j in range(m):
            if arr[i][j] == 1:
                q.append((k, i, j))
    pan.append(arr)


def bfs():
    global q

    while q:
        # print(pan)
        k, i, j = q.popleft()

        for d in range(6):
            ni, nj, nk = i + dx[d], j + dy[d], k + dz[d]

            if 0 <= ni < n and 0 <= nj < m and 0 <= nk < h: # 범위 내에 있는 경우
                if pan[nk][ni][nj] == 0:
                    # 인접 토마토가 아직 익지 않은 토마토이고 방문한적 없는 경우
                    pan[nk][ni][nj] = pan[k][i][j] + 1 # 익은 토마토의 정수 값 + 1
                    q.append((nk, ni, nj))
                else:
                    continue


# 토마토 농사 시작
bfs()

ans = 0
for k in pan:
    for i in k:
        if 0 in i:
            print(-1)
            exit()

        ans = max(ans, max(i))

print(ans-1)
