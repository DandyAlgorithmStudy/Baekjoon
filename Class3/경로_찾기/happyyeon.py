from collections import deque

N = int(input())
graph = [[0]*N for _ in range(N)]

for i in range(N):
    line = input().replace(" ","")
    for j in range(N):
        graph[i][j] = int(line[j])

def bfs(start):
    visited = [0]*N
    q = deque([start])

    while q:
        cur = q.popleft()

        for i in range(N):
            if graph[cur][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
    
    return visited

for node in range(N):
    print(*bfs(node))

