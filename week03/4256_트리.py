import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 전위 순회(preorder) : root -> left -> right
# 중위 순회(inorder) : left -> root -> right
# 후위 순회(postorder) : left -> right -> root

post_order = [] 
def find_post(pre_s, pre_e, in_s, in_e):
    if pre_s > pre_e or in_s > in_e:
        return


    root_index = pre_order[pre_s]
    post_order.append(root_index)
    
    in_index = 0
    for i in range(n):
        if in_order[i] == pre_order[pre_s]:
            in_index = i

    len_left = in_index
    len_right = len(pre_order) - in_index - 1

    find_post(len_left + 1, pre_e, in_s ,in_e ) # right부분
    find_post(pre_s + 1, pre_s + 1 + len_left, pre_s, pre_s + len_left - 1) # left부분


t = int(input().rstrip())
for _ in range(t):
    n = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))

    find_post(0, n, 0, n)
    post_order.reverse()
    print(*post_order)





#######################
from sys import stdin
import sys

sys.setrecursionlimit(10**9)

# 전위 순회(preorder) : root -> left -> right
# 중위 순회(inorder) : left -> root -> right
# 후위 순회(postorder) : left -> right -> root

def go(pre_start, pre_end, in_start, in_end):
    if pre_start>pre_end or in_start>in_end:
        return

    root = preorder[pre_start]
    postorder.append(root)
    index = inorder_index[root]

    left_len = index - in_start
    right_len = in_end - index

    #right first
    go(pre_end - right_len +1 , pre_end, index+1, in_end)
    go(pre_start+1, pre_start + left_len, in_start, index-1)



for _ in range(int(input())):
    n = int(input())

    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))

    inorder_index = [0] * (n+1)
    for i in range(n):
        inorder_index[inorder[i]] = i

    postorder = []

    go(0, n-1, 0, n-1)
    postorder.reverse()
    print(' '.join(map(str,postorder))) 