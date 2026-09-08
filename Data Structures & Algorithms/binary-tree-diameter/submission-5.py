class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:

            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:

            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        left_dia = self.diameterOfBinaryTree(root.left)
        right_dia = self.diameterOfBinaryTree(root.right)

        current_diameter = left_height + right_height

        return max(current_diameter, left_dia + right_dia)
