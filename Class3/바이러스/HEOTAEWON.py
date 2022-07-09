import sys
from collections import deque
sys.stdin = open('input', 'r')

n = int(input())
k = int(input())

check = [False] * (n+1)
pan = list([False] * (n+1) for _ in range(n+1))
q = deque()
visited = []
def virus():
    q.append(1)
    while q:
        a = q.popleft()
        for i in range(1, n+1):
            if pan[a][i]:
                if (a, i) not in visited:
                    q.append(i)
                    visited.append((a, i))
                    check[i] = True
    return





    # for i in range(1, n+1):
    #     if pan[a][i]: # 입력받은 숙주 컴퓨터 탐색시작, 감염 시 check에 표시
    #         check[i] = True
    #         virus(i, pan) # 감염된 컴퓨터를 숙주로 다시 전파시작
    # return


# 연결된 node 마킹(2차원)
for _ in range(k):
    a, b = map(int, input().split())
    pan[a][b] = True
    pan[b][a] = True

ans = 0
virus()

for i in range(1, n+1):
    if check[i]:
        ans += 1
# print(check)
print(ans-1)
