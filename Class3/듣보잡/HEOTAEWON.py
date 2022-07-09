import sys

sys.stdin = open('input', 'r')

n, m = map(int, input().split())
no_listened = set()
ans = []
for _ in range(n):
    no_listened.add(input())

for _ in range(m):
    no_see = input()
    if no_see in no_listened:
        ans.append(no_see)

ans.sort()
print(len(ans))
for i in ans:
    print(i)
