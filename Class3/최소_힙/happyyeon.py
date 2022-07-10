import sys
import heapq as h

input = sys.stdin.readline
test_case = int(input())

heap = []
for _ in range(test_case):
    command = int(input())

    if command > 0:
        h.heappush(heap,command)
    
    if command == 0:
        if not heap:
            print(0)
        else:
            print(h.heappop(heap))