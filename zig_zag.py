# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag(root):
    if root is None:
        return []
    q = [root]
    ans = []
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.val)
        ans.append(level)
    for i in range(len(ans)):
        if i % 2 == 1:
            ans[i] = ans[i][::-1]
    return ans

if __name__ == "__main__":


    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(zigzag(root))
