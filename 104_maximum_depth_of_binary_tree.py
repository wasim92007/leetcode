# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ## Method 3: Using depth first search (pre-order DFS)
        ## Main idea is we will start with a node, pop it out and add it's children and continue
        if not root: ## A leaf node
            return 0
        else:
            stack = [[root, 1]]
            res = 1
            
            while stack:
                node, depth = stack.pop()
                ## If the node is not None
                if node:
                    ## Update the depth
                    res = max(res, depth)
                    
                    ## Add the children
                    if node.left:
                        stack.append([node.left, depth + 1])
                    if node.right:
                        stack.append([node.right, depth + 1])
            return res
        
        
        ## Method 2: Using breadth first search
        if not root: ## A leaf node
            return 0
        else:
            ## Value and queue intialization
            level = 0 ## Setting the intial value to 0, this will be incremented after removal
            q = deque([root]) ## Intializing the queue with root node
            
            ## Traversing the q
            while q:
                ## Now we want to go trhough the queue and remove every
                ## element that are currently in it
                
                ## So however many hence
                for i in range(len(q)):
                    node = q.popleft()
                    ## Add the children of the removed node to the right
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
                ## Once we are done with that level we are going to increase the level
                level += 1
                
            ## We have completed going through all the nodes at all the levels    
            return level
            
            
        
        ## Method 1: Using recursion
        if not root: ## A leaf node
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
