INF = int(1e9)
region, search, road = map(int,input().split())

item = list(map(int,input().split()))

graph = [[INF]*region for _ in range(region)]

for i in range(road):
    start,end,distance = map(int,input().split())

    graph[start-1][end-1] = distance
    graph[end-1][start-1] = distance

for i in range(region):
    graph[i][i] = 0

# 플로이드 와샬 알고리즘
for i in range(region):
    for j in range(region):
        for k in range(region):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]


lst_answer = []
for i in range(region):
    count = 0
    for j in range(region):
        if graph[i][j] <= search:
            count += item[j]
    lst_answer.append(count)

print(max(lst_answer))
