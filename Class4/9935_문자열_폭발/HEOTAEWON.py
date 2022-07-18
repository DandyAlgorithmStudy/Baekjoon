import sys

sys.stdin = open('input', 'r')

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
bomb_list = [i for i in bomb]
check = []
length = len(bomb)

for i in string: # 입력 문자열의 처음부터 마지막까지
    check.append(i)
    if i == bomb[-1]: # 폭탄의 마지막과 일치한다면
        # print(check[len(check)-length:len(check)])
        if check[len(check)-length:len(check)] == bomb_list: # 폭탄이 들어있다면
            for _ in range(length):
                check.pop(-1)

if len(check) == 0:
    print('FRULA')
else:
    print(''.join(check))


##### 최초시도: 문자열 replace 함수 사용
# flag = 0
#
# while not flag: # flag가 올라올떄까지 반복
#     # print(string)
#     if bomb in string:
#         # print('폭발')
#         string = string.replace(bomb, '') # 폭발물 공란으로 대체해준다.
#     else:
#         if bomb not in string:
#             flag = 1
#
# if string == '':
#     print('FRULA')
# else:
#     print(string)
