import heapq as h
import sys
input = sys.stdin.readline
INF = int(1e9)
city = int(input())
bus = int(input())

graph = [[] for _ in range(city+1)]

for i in range(bus):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start,end = map(int,input().split())
####



def dijkstra(start):
    distance = [INF]*(city+1)
    heap = []
    h.heappush(heap,(0,start))
    distance[start] = 0
    path = [[] for _ in range(city+1)] # 경로
    path[start].append(start)

    while heap:
        dist,now = h.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                h.heappush(heap,(cost,i[0]))
                path[i[0]] = []
                for j in path[now]:
                    path[i[0]].append(j)
                path[i[0]].append(i[0])
    
    return distance,path

distance,path = dijkstra(start)
print(distance[end])
print(len(path[end]))
print(" ".join(map(str,path[end])))


