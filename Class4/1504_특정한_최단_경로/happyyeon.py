import heapq as h
import sys
input = sys.stdin.readline
INF = int(1e9)
## 문제 조건 세팅 ##
N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())
####

# 다익스트라 알고리즘
# 특정 노드 --> 특정 노드 최단 경로를 구하기 위하여
# 시간복잡도를 줄이기 위하여 힙을 사용
def dijkstra(start):
    distance = [INF]*(N+1)
    heap = []
    h.heappush(heap,(0,start))
    distance[start] = 0

    while heap:
        dist,now = h.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                h.heappush(heap,(cost,i[0]))
    
    return distance

# === 노드 1 --> 노드 N (v1,v2 경유) ===
# 노드 1 --> 노드 v1 최단 경로
# 노드 v1 --> 노드 v2 최단 경로
# 노드 v2 --> 노드 N 최단 경로
# =======================================

sum1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N]

sum2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N]

answer = min(sum1,sum2)

if answer >= INF:
    print(-1)
else:
    print(answer)