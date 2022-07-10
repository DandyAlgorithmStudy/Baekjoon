from collections import deque
node = int(input())
edge = int(input())

# 컴퓨터 연결망 초기화
graph = [[0]*(node+1) for _ in range(node+1)]
visited = [0]*(node+1)

# 컴퓨터 연결망 상태 표시
for _ in range(edge):
    start,end = map(int,input().split())

    graph[start][end] = 1
    graph[end][start] = 1

# 그래프 탐색
def bfs(start):
    q =deque([start])
    visited[start] = 1
    count = 0

    while q:
        cur = q.popleft()

        for i in range(node+1):
            if graph[cur][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
                count += 1
    
    return count

print(bfs(1))
                

