import sys
input = sys.stdin.readline
from itertools import combinations
INF = int(1e9)
N, M = map(int,input().split())

house = []
chicken = []

for i in range(N):
    temp = list(map(int,input().split()))

    for j in range(N):
        if temp[j] == 1:
            house.append((i,j))
        if temp[j] == 2:
            chicken.append((i,j))

answer = INF
for c in combinations(chicken,M):
    city_distance = 0
    for h in house:
        chicken_distance = INF
        for i in range(M):
            chicken_distance = min(chicken_distance,abs(c[i][0]-h[0])+abs(c[i][1]-h[1]))
        city_distance += chicken_distance
    answer = min(answer,city_distance)

print(answer)


 

