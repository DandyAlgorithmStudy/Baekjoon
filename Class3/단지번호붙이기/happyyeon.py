from collections import deque

n = int(input())
graph = [[0]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    house_info = input()
    for j in range(n):
        graph[i][j] = int(house_info[j])

def bfs(x,y):
    house_count = 0
    q = deque([[x,y]])
    graph[x][y] = 2
    while q:
        cur_node = q.popleft()
        house_count += 1

        for i in range(4):
            new_x = cur_node[0]+dx[i]
            new_y = cur_node[1]+dy[i]

            if 0<=new_x<n and 0<=new_y<n:
                if graph[new_x][new_y] == 1:
                    q.append([new_x,new_y])
                    graph[new_x][new_y] = 2
    
    return house_count

lst_answer = []

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            lst_answer.append(bfs(x,y))
lst_answer.sort()
print(len(lst_answer))
for answer in lst_answer:
    print(answer)
    