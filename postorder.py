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
    postorder(root)

def postorder(root):
    if root == None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')

# Input and create BST
arr = list(map(int, input().split()))
createBST(arr)
print()

