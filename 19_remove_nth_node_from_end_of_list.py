# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ## Get the lengh of the linked list
        l = 0
        
        ## Use a temp_node
        temp_node = head
        
        ## Get the length of the Linked list
        while temp_node:
            l+=1; temp_node = temp_node.next
        
        ## If there is one node or
        ## n is equal to the l, i.e.,
        ## we are removing the first node
        ## then we should return None
        if l - n == 0:
            return head.next
        
        ## We will start traversing from the begining
        ## As we are already at the head node, we need
        ## to traverse l - n - 1 position to reach the
        ## previous node to the node which want to remove
        l = l - n - 1
        temp_node = head
        #l =3
        
        while l > 0:
            temp_node = temp_node.next; l -=1
            
        temp_node.next = temp_node.next.next
            
        
        return head
