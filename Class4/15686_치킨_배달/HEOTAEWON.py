import sys
from itertools import combinations

sys.stdin = open('input', 'r')

n, m = map(int, input().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

house = []
chicken = []

# 집과 치킨집 좌표를 각각 저장한다.
for i in range(n):
    for j in range(n):
        if pan[i][j] == 1:
            house.append((i, j))
        elif pan[i][j] == 2:
            chicken.append((i, j))

# 중복 없이 m개의 치킨집을 고르는 경우의 수
chicken_select = list(combinations(chicken, m))
ans = 999999

for c in chicken_select:  # m개 선택된 치킨집의 모든 경우의 수
    distance = 0 # 거리 초기화
    for h in house:  # 집의 좌표가 튜플로 반환
        select = [] # 선택된 치킨집들과 집까지의 치킨거리를 저장해줄 리스트
        for i in range(m): # 각 경우의 수마다 선택된 치킨집들을 모두 탐색
            select.append((abs((h[0]-c[i][0])) + abs((h[1]-c[i][1])))) # 치킨거리를 추가
        distance += min(select) # 해당 집의 치킨거리중 최솟값을 더해줌
    # print(distance)
    if distance < ans: # 모든 경우의 수에 따른 도시의 치킨거리중 최솟값을 선택
        ans = distance

print(ans)


