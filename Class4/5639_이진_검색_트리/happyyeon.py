import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

### 문제 조건 ###
binary_tree = []
while True:
    try:
        binary_tree.append(int(input()))
    except:
        break
### ###

# BST 후위 순회
def post_order(start,end):
    if start > end:
        return
    root = end+1 # 오른쪽 Sub Tree가 없을 경우를 대비

    for i in range(start+1,end+1):
        # 오른쪽 Sub Tree 발견
        if binary_tree[i] > binary_tree[start]:
            root = i
            break
    
    post_order(start+1,root-1) # 왼쪽 Sub Tree Traverse
    post_order(root,end) # 오른쪽 Sub Tree Traverse

    print(binary_tree[start])

post_order(0,len(binary_tree)-1)


