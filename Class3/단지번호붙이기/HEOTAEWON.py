import sys
from collections import deque

sys.stdin = open('input', 'r')

n = int(input())
pan = [list(map(int, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
area = 0
ans = []


def bfs(x, y, pan):
    global area
    q = deque()
    visited = []
    q.append((x, y))
    visited.append((x, y))
    check[x][y] = 1

    while q:
        i, j = q.popleft()

        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n: # 만약 범위 내에 있다면
                if pan[nx][ny] == 1 and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.append((nx, ny))
                    check[nx][ny] = 1
    area += 1

    ans.append(len(visited))
    return


for i in range(n):
    for j in range(n):
        if pan[i][j] == 1 and check[i][j] == 0:
            bfs(i, j, pan)
        else:
            continue

ans.sort()
print(area)
for num in ans:
    print(num)
