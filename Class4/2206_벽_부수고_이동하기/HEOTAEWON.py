import sys
from collections import deque

sys.stdin = open('input', 'r')

n, m = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

q = deque()
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(): # 벽을 부수지 않는 경우
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()

        if x == n-1 and y == m-1: # 목적지에 도달한 경우
            return visited[x][y][wall] # 시작점이 0이므로 1을 더해서 반환해준다.

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내에 있고 아직 방문한 적 없다면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                if pan[nx][ny] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))

                elif wall == 0 and pan[nx][ny] == 1:
                    visited[nx][ny][wall+1] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall+1))

    return -1


print(bfs())

## 시간초과 해결법:
# pan을 수정하고 visited에 따로 추가하는 방법대신
# pan에는 벽과 이동가능 여부만 확인하고
# visited를 초기화해가면서 visited 3차원 배열을 이용해서 이동한다.

## 메모리초과 해결법:
# 제일 처음 if문 조건에 방문한적 있는지의 여부를 확인하고 queue에 append 해야한다.
