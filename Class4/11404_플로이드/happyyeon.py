cities = int(input())
buses = int(input())
INF = int(1e9)
graph = [[INF]*(cities+1) for _ in range(cities+1)]


for i in range(buses):
    start, end, cost = map(int,input().split())

    # 같은 경로의 버스가 여러 개 존재할 수 있다는 사실을 주의 !!
    if graph[start][end] != INF:
        graph[start][end] = min(graph[start][end], cost)
    else:
        graph[start][end] = cost

for i in range(cities+1):
    graph[i][i] = 0

# 플로이드 와샬 알고리즘
for i in range(cities+1):
    for j in range(cities+1):
        for k in range(cities+1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]



# 정답 출력
for i in range(1,cities+1):
    for j in range(1,cities+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()