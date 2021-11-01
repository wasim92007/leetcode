# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ## without using any set
        ## Floyd's Tortoise and Hare method
        ## https://www.youtube.com/watch?v=gBTe7lFR3vc
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            ## If there is a cycle at some point in time
            ## slow and fast will point to the same node
            if slow == fast:
                return True
        return False
        
        ##################################################
        ## We will maintain a set of node
        val_pos = set()
        
        ## We will traverse through the linked list till
        ## either it ends or we detect a cycle
        while head:
            ## if the next node is already in the set then
            ## we have a loop
            if head.next in val_pos:
                return True
            ## Otherwise keep on adding the current node to
            ## the linked list
            else:
                val_pos.add(head) 
                head = head.next
                
        ## Return false in case we have not found any loop
        return False
