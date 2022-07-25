import sys
from collections import deque
input = sys.stdin.readline

# 문제 초기 조건
N,T,G = map(int,input().split())
###

if N > G:
    print("ANG")
    exit(0)

# B 버튼
def button_b(num):
    temp = str(2*num)

    if 0<=int(temp)<MAXIMUM:
        if int(temp) != 0:
            temp = str(int(temp[0])-1) + temp[1:]

    return int(temp)
# 0~99999 그래프 생성
MAXIMUM = 100000
visited = [False]*MAXIMUM

# N --> G 최단거리
def bfs(start):
    q = deque([start])
    count = [0]*MAXIMUM
    visited[start] = True

    while q:
        cur = q.popleft()
        # print("현재 카운트:{0}, 현재 노드: {1}".format(count[cur], cur))
        if count[cur] > T:
            return "ANG"
    
        if cur == G:
            return count[cur]

        a = cur+1
        b = button_b(cur)

        if 0<=a<MAXIMUM:
            if visited[a] == False:
                q.append(a)
                visited[a] = True
                count[a] = count[cur] + 1
        if 0<=b<MAXIMUM:
            if visited[b] == False:
                q.append(b)
                visited[b] = True
                count[b] = count[cur] + 1
    
    return "ANG"
        
answer = bfs(N)

print(answer)