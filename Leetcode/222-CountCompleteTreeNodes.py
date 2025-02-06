class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def countCompleteTreeNodes(root):
        if not root:
            return 0
        left = Solution.countCompleteTreeNodes(root.left)
        right = Solution.countCompleteTreeNodes(root.right)
        return 1 + left + right


root = [1, 2, 3, 4, 5, 6]
print(Solution.countCompleteTreeNodes(root))
