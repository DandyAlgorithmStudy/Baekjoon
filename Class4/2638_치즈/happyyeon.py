from collections import deque
N,M = map(int,input().split())

cheese = []

for _ in range(N):
    cheese.append(list(map(int,input().split())))



dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    q = deque([(a,b)])
    visited = [[0]*M for _ in range(N)]
    touch = [[0]*M for _ in range(N)]
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                
                if cheese[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                
                if cheese[nx][ny] == 1:
                    touch[nx][ny] += 1
    
    for i in range(N):
        for j in range(M):
            if touch[i][j] >= 2:
                cheese[i][j] = 0

def empty_check(cheese):
    
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                return False
    return True

hour = 0

while True:

    if empty_check(cheese):
        print(hour)
        break

    bfs(0,0)
    hour += 1


    
    
                    
            


