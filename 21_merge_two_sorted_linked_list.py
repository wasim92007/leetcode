# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## Create a dummy Node
        dummy = ListNode()
        
        tail = dummy
        
        
        ##print(l1)
        ##> ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
        ## Iterate over as long as both of them are not None
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        
        ## When one of the Node is empty
        if l1:
            tail.next = l1
        else:
            tail.next = l2
            
        return dummy.next
