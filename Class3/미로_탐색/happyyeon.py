from collections import deque
N,M = map(int,input().split())

# 미로 초기화
graph = [[0]*M for _ in range(N)]

# 미로 정보 입력
for i in range(N):
    line = input()
    for j in range(M):
       graph[i][j] = int(line[j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# BFS
def bfs(x,y):
    q = deque([(x,y)])
    
    while q:
        cur = q.popleft()
        ox,oy = cur[0],cur[1]

        # 정답을 찾은 Case
        if cur == (N-1,M-1):
            break

        # 정답을 찾아가는 과정
        for i in range(4):
            nx = cur[0]+dx[i]
            ny = cur[1]+dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[ox][oy] + 1

bfs(0,0)

print(graph[N-1][M-1])

