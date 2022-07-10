import sys
import heapq as h
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    num = int(input())

    if num > 0:
        h.heappush(heap,[num,True])
    
    if num < 0:
        h.heappush(heap,[-1*num,False])

    if num == 0:
        if not heap:
            print(0)
        else:
            element = h.heappop(heap)

            answer, flag = element[0], element[1]

            if flag == True:
                print(answer)
            else:
                print(-1*answer)
