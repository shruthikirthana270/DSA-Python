class Node:
    def __init__(self, data):
        self.left = None
        self.val = data
        self.right = None

def createBST(arr):
    root = None
    for data in arr:
        if root is None:
            root = Node(data)
        else:
            temp = root
            while True:
                if data < temp.val:
                    if temp.left == None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
                elif data > temp.val:
                    if temp.right == None:
                        temp.right = Node(data)
                        break
                    else:
                        temp = temp.right
                else:
                    break
    preorder(root)

def preorder(root):
    if root == None:
        return
    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)

# Input and create BST
arr = list(map(int, input().split()))
createBST(arr)
print()

