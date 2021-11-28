n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def print_preorder(inorder, postorder):
    mid = postorder[-1]
    left = inorder[:mid]
    right = inorder[mid+1:]
    
    if 

    print(mid, end='')
    print_preorder()