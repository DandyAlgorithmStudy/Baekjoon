import sys
from math import inf
import heapq

sys.stdin = open('input', 'r')

n, e = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b)) # a에서 b로 가는데 c만큼 걸린다.
    graph[b].append((c, a))


v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start):
    q = []
    distance = [inf] * (n+1) # 최단거리를 갱신해나갈 리스트
    distance[start] = 0
    heapq.heappush(q, (0, start)) # 거리를 가장 우선적으로 heap 정렬하기 위해 거리정보를 튜플의 첫번째 인자로 받는다.

    while q:
        d, temp = heapq.heappop(q) # 가장 우선적으로 가까운 지점과 거리를 pop한다.

        if distance[temp] < d: # 만약 거쳐갈 지점까지의 거리가 기존의 거리보다 멀면 continue
            continue
        for i in graph[temp]: # 거쳐갈 지점까지의 거리가 기존의 거리보다 가깝다면
            dist = d + i[0] # 거쳐가는만큼 거리를 더해준다.
            if dist < distance[i[1]]: # 만약 거쳐지나가는 거리의 합이 기존의 해당 지점까지의 거리보다 가깝다면
                distance[i[1]] = dist # 갱신해준다.
                ##### 이 부분이 잘 이해안됨
                heapq.heappush(q, (dist, i[1]))

    return distance


path_1 = dijkstra(1)
path_v1 = dijkstra(v1)
path_v2 = dijkstra(v2)

ans_1 = path_1[v1] + path_v1[v2] + path_v2[n]
ans_2 = path_1[v2] + path_v2[v1] + path_v1[n]

if ans_1 >= inf and ans_2 >= inf:
    print(-1)
else:
    print(min(ans_1, ans_2))
