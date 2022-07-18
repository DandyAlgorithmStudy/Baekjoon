import sys
from math import inf
sys.stdin = open('input', 'r')

n, m, r = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))
print(item)

graph = [[inf] * (n+1) for _ in range(n+1)] # 순수 입력

for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    # a에서 b로 가는 길은 양방향이기 때문에 서로 똑같다.
    graph[a][b] = c
    graph[b][a] = c

#### 플로이드 워셜 알고리즘 ####

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: # 출발지줨과 목적지가 같다면
                graph[i][j] = 0
            # i에서 j로 가는 경우 k를 거쳐서 갈때 더 짧다면 업데이트 해준다.
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = []

for i in range(1, n+1):
    item_cnt = 0
    for j in range(1, n+1):
        if graph[i][j] <= m: # 수색 가능한 곳이라면
            item_cnt += item[j-1] # 해당 지역의 아이템 수를 더해준다.
    ans.append(item_cnt)

print(max(ans))
