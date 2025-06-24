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
                    if temp.left is None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
                elif data > temp.val:
                    if temp.right is None:
                        temp.right = Node(data)
                        break
                    else:
                        temp = temp.right
    return root

def levelorder_print(root):
    if root is None:
        return
    q = [root]
    while q:
        node = q.pop(0)
        print(node.val, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# Direct input array
arr = [10, 5, 15, 3, 7, 12, 18]
root = createBST(arr)
levelorder_print(root)
