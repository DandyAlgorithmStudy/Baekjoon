import sys
from math import inf

sys.stdin = open('input', 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] > c: # 기존의 거리보다 짧다면 갱신해준다.
        graph[a-1][b-1] = c

# print(graph)
for k in range(n):
    for i in range(n):
        for j in range(n):
            # i에서 j로 갈때 k를 거쳐가는 경우가 더 짧다면 갱신해준다.
            if i == j:
                graph[i-1][j-1] = 0
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in graph:
    for j in i:
        if j >= inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()

