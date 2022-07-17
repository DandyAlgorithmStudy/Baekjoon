import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())

graph = [[0]*M for _ in range(N)]
# visited[x][y][0] --> 벽 파괴 기회 O
# visited[x][y][1] --> 벽 파괴 기회 X
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

# 맵 생성
for i in range(N):
    line = input()
    for j in range(M):
        graph[i][j] = int(line[j])


dx = [1,-1,0,0]
dy = [0,0,1,-1]

# BFS로 최단거리 탐색
def bfs(a,b,c):
    visited[a][b][c] = 1
    q = deque([(a,b,c)])

    while q:
        x,y,z = q.popleft()

        # 끝 지점 도달
        if x == N-1 and y == M-1:
            return visited[x][y][z]

        # 상하좌우 탐색 해봄
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny][z] == 0:
                # Case1. 벽 & 벽 파괴 기회 O
                # --> (nx,ny) 벽 파괴 기회 삭제 & 큐에 추가(이동)
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx,ny,1))

                # Case2. 벽 & 벽 파괴 기회 X
                # --> 이동 불가

                # Case3. 길
                # --> 이동
                if graph[nx][ny] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx,ny,z))
    
    return -1

print(bfs(0,0,0))











