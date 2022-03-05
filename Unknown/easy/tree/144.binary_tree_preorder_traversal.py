#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Easy (61.59%)
# Likes:    3756
# Dislikes: 117
# Total Accepted:    878.4K
# Total Submissions: 1.4M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ## Preorder traversal is root->left->right
        ## https://www.youtube.com/watch?v=RJhh3Jcc9zw
        ## Algorithm 2: We will use iteration
        ## We will be using stack: stack is last in first out
        ## We will put in stack = [right, left]
        result = []
        if root is None:
            return result
        stack = [root]

        ## while stack is not empty
        while stack != []:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

        ## Algorithm 1: We will use recursion
        ## Base case: If root is None
        if root is None:
            return []
        else:
            return [root.val] + self.preorderTraversal(root=root.left) + self.preorderTraversal(root=root.right)



        
# @lc code=end

