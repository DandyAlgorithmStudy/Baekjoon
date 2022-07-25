import sys
input = sys.stdin.readline

# 초기 조건
n = int(input())
port = list(map(int,input().split()))

# 정렬된 배열에서 value가 위치할 수 있는 가장 작은 index
def lower_bound(start,end,value,arr):
    while start < end:
        mid = (start+end)//2

        if arr[mid] < value:
            start = mid+1
        else:
            end = mid
    
    return end

lis = []

for i in range(n):
    if i == 0:
        lis.append(port[i])
    else:
        if lis[-1] < port[i]:
            lis.append(port[i])
        else:
            idx = lower_bound(0,len(lis),port[i],lis)
            lis[idx] = port[i]

print(len(lis))