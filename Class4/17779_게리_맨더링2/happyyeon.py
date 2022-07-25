import sys
input = sys.stdin.readline
INF = int(1e9)
# Initialize
N = int(input())
city = []
for i in range(N):
    city.append(list(map(int,input().split())))

total = 0 # 총원
for i in range(N):
    for j in range(N):
        total += city[i][j]

def sol(x,y,d1,d2):
    temp = [[0]*N for _ in range(N)]
    # 선거구 5 세팅
    for i in range(d1+1):
        temp[x+i-1][y-i-1] = 5
        temp[x+d2+i-1][y+d2-i-1] = 5
    for i in range(d2+1):
        temp[x+i-1][y+i-1] = 5
        temp[x+d1+i-1][y-d1+i-1] = 5


    max_people = -1*INF
    min_people = INF
    
    sum1 = 0
    # 선거구 1 세팅
    for i in range(1,x+d1):
        for j in range(1,y+1):
            if temp[i-1][j-1] == 5:
                break
            # 선거구 1 인원
            sum1 += city[i-1][j-1]
    
    # Max Min Update
    if max_people < sum1:
        max_people = sum1

    if min_people > sum1:
        min_people = sum1
    
    sum2 = 0
    # 선거구 2 세팅 (열의 개수가 점점 작아지므로 역탐색 해야함)
    for i in range(1,x+d2+1):
        for j in range(N,y,-1):
            if temp[i-1][j-1] == 5:
                break

            # 선거구 2 인원
            sum2 += city[i-1][j-1]
    
    # Max Min Update
    if max_people < sum2:
        max_people = sum2

    if min_people > sum2:
        min_people = sum2
    
    # 선거구 3 세팅
    sum3 = 0
    for i in range(x+d1,N+1):
        for j in range(1,y-d1+d2):
            if temp[i-1][j-1] == 5:
                break
            # 선거구 3 인원
            sum3 += city[i-1][j-1]
    
    # Max Min Update
    if max_people < sum3:
        max_people = sum3

    if min_people > sum3:
        min_people = sum3
    
    sum4 = 0
    # 선거구 4 세팅 (열의 개수가 점점 작아지므로 역탐색 해야함)
    for i in range(x+d2+1,N+1):
        for j in range(N,y-d1+d2-1,-1):
            if temp[i-1][j-1] == 5:
                break

            # 선거구 4 인원
            sum4 += city[i-1][j-1]
    
    # Max Min Update
    if max_people < sum4:
        max_people = sum4

    if min_people > sum4:
        min_people = sum4
    
    # 선거구 5 인원
    sum5 = total - sum1 - sum2 - sum3 - sum4

    # Max Min Update
    if max_people < sum5:
        max_people = sum5

    if min_people > sum5:
        min_people = sum5
    
    return max_people-min_people

min_answer = INF

for d1 in range(1,N):
    for d2 in range(1,N):
        for x in range(1,N-d1-d2+1):
            for y in range(d1+1,N-d2+1):
                answer = sol(x,y,d1,d2)

                if min_answer > answer:
                    min_answer = answer

print(min_answer)