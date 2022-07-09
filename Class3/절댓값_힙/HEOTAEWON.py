import sys
import heapq

sys.stdin = open('input', 'r')

n = int(sys.stdin.readline())
min_heap = []
max_heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(min_heap, x)
    elif x < 0:
        heapq.heappush(max_heap, -x)
    elif x == 0:
        if len(min_heap) == 0 and len(max_heap) == 0: # 둘 다 비어있는 경우
            print(0)
        elif len(min_heap) > 0 and len(max_heap) == 0: # max_heap이 비어있는 경우
            print(heapq.heappop(min_heap))
        elif len(min_heap) == 0 and len(max_heap) > 0: # min_heap이 비어있는 경우
            print(-heapq.heappop(max_heap))
        elif len(min_heap) > 0 and len(max_heap) > 0: # 둘다 비어있지 않은 경우
            a, b = min_heap[0], max_heap[0] # 두 heap의 최솟값을 받아온다.
            if a > b: # max_heap의 절댓값이 더 작은 경우
                print(-heapq.heappop(max_heap))
            elif a < b: # min_heap의 절댓값이 더 작은 경우
                print(heapq.heappop(min_heap))
            elif a == b: # 두 값의 절댓값이 같은 경우
                print(-heapq.heappop(max_heap))
