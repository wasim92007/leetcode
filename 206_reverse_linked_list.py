# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ## By passing the case if empty linked list
        if not head:
            return head
        else:
            ## We will be using two nodes method with prev and curr
            ## intialized to None and head respectively
            prev, curr = None, head
            
            ## We will be traversing throught the linked list
            while curr:
                ## Let us temporalily save the rest of the linked list
                ## right to the curr node in rest_ll
                rest_ll = curr.next
                
                ## Make the curr point to the pre
                curr.next = prev
                ## Prev point to the curr
                prev = curr
                ## Update curr to point to the rest of the ll
                curr = rest_ll
            
            return prev
