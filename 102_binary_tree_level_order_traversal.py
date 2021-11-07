# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ## Queue, result intialization
        q = deque([root])
        result = []
        
        ## Traversing the q
        while q:
            ## Intializing level_nodes
            level_nodes = []
            
            ## Now we want to go through the queue and remove every
            ## element that are currently in it
                
            ## So however many hence
            for i in range(len(q)):
                node = q.popleft()
                ## Adding the nodes at that level
                level_nodes.append(node.val)
                ## Add the children of the removed node to the right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            ## Adding the level nodes to main result
            result.append(level_nodes)
        
        return result
