import sys

sys.stdin = open('input', 'r')
sys.setrecursionlimit(10 ** 6)

tree = []

while True:
    try:
        n = int(input())
        tree.append(n)
    except:
        break


def recurs(start, end):
    if start >= end:
        return

    root = tree[start]
    temp = 0

    if tree[end-1] <= root:
        recurs(start+1, end)
        print(root)
        return

    for i in range(start+1, end):
        if tree[i] > root: # 트리의 루트보다 커지는 경우
            temp = i
            break

    recurs(start+1, temp)
    recurs(temp, end)
    print(root)

# print(tree)
recurs(0, len(tree))
