import sys
from collections import deque
input = sys.stdin.readline

# 초기 조건
m,n,h = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append((i,j,k))

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(tomato):
    while q:
        i,j,k = q.popleft()

        for dir in range(6):
            x = i+dx[dir]
            y = j+dy[dir]
            z = k+dz[dir]
        
            if 0<=x<h and 0<=y<n and 0<=z<m and tomato[x][y][z] == 0:
                tomato[x][y][z] = tomato[i][j][k] + 1
                q.append((x,y,z))

def check_zero(tomato):
    for i in range(h):
        for j in tomato[i]:
            if 0 in j:
                return True
        return False

def check_day(tomato):
    day = 0

    for i in range(h):
        for j in tomato[i]:
            day = max(max(j),day)
    return day


bfs(tomato)


day = 0
for i in tomato:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)