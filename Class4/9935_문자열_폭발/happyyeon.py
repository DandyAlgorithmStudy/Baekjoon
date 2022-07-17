### 문제 조건 & 1번###
string = []
temp = input()
for i in range(len(temp)):
    string.append(temp[i])
bomb = []
temp = input()
for i in range(len(temp)):
    bomb.append(temp[i])
######

stack = []
count = 0

for i in range(len(string)):
    stack.append(string[i])
    count += 1

    if count >= len(bomb):
        for j in range(count-len(bomb),count):
            if stack[j] != bomb[j-count]:
                break
        else:
            for k in range(len(bomb)):
                stack.pop()
                count -= 1

if not stack:
    print("FRULA")
else:
    print("".join(stack))





