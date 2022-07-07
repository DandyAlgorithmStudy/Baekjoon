from collections import defaultdict

hear, see = map(int,input().split())

name_count = defaultdict(int)

for _ in range(hear+see):
    name = input()
    name_count[name] += 1

lst_answer = []
for name in name_count:
    if name_count[name] >= 2:
        lst_answer.append(name)

lst_answer.sort()

print(len(lst_answer))
for answer in lst_answer:
    print(answer)


    
