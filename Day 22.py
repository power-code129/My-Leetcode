#Given the root of a binary tree, return the inorder traversal of its nodes' values.
#Example 1:
#Input: root = [1,null,2,3]
#Output: [1,3,2]

#Example 2:
#Input: root = []
#Output: []

#Example 3:
#Input: root = [1]
#Output: [1]

#Constraints:

#The number of nodes in the tree is in the range [0, 100].
#-100 <= Node.val <= 100
 

#Follow up: Recursive solution is trivial, could you do it iteratively?


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right

# Example usage:
# sol = Solution()
# root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
# print(sol.inorderTraversal(root))  # Output: [1, 3, 2]
