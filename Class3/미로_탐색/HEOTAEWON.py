import sys
from collections import deque

sys.stdin = open('input', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
pan = [list(map(int, input())) for _ in range(n)]
# print(pan)

q = deque()
q.append((0, 0))
visited = []

while q:
    x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(pan[x][y])
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if pan[nx][ny] == 0 and (nx, ny) in visited :
                continue
            if pan[nx][ny] == 1:
                pan[nx][ny] = pan[x][y] + 1
                q.append((nx, ny))










# q = deque()
# visited = [(0, 0, 1)]
# q.append((0, 0, 1))
#
# while q:
#     x, y, dist = q.popleft()
#     if x == n-1 and y == m-1:
#         print(dist)
#         break
#     for i in range(4): # 상하좌우 탐색
#         nx, ny = x + dx[i], y + dy[i]
#         if nx == n-1 and ny == m-1:
#             print(dist+1)
#             exit()
#         if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있다면
#             # print(nx, ny)
#             if (nx, ny, dist+1) not in visited and pan[nx][ny] == '1':# 방문한적 없는 좌표이고 이동할 수 있다면
#                 q.append((nx, ny, dist+1))
#                 visited.append((nx, ny, dist+1))
#             else:
#                 continue
