# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ## My method optimized
                ## My method
        head = ListNode()
        temp = head
        
        carry = 0
        while l1 or l2 or carry:
            #print('l1.val', l1.val)
            #print('l2.val', l2.val)
            #print('l1.val + l2.val', l1.val + l2.val)
            t = ListNode()
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            t.val = (carry + v1 + v2)%10
            carry = (carry + v1 + v2)//10
            temp.next = t
            l1, l2, temp = l1.next if l1 else None, l2.next if l2 else None, temp.next
        
        head = head.next
        return head
        
        
        ## My method
        head = ListNode()
        temp = head
        
        carry = 0
        while l1 and l2:
            #print('l1.val', l1.val)
            #print('l2.val', l2.val)
            #print('l1.val + l2.val', l1.val + l2.val)
            t = ListNode()
            t.val = (carry + l1.val + l2.val)%10
            carry = (carry + l1.val + l2.val)//10
            temp.next = t
            l1, l2, temp = l1.next, l2.next, temp.next
            
        if l1:
            rem = l1
        else:
            rem = l2
        while rem:
            #print('l1.val', l1.val)
            #print('l2.val', l2.val)
            #print('l1.val + l2.val', l1.val + l2.val)
            t = ListNode()
            t.val = (carry + rem.val)%10
            carry = (carry + rem.val)//10
            temp.next = t
            rem, temp = rem.next, temp.next
            
        if carry > 0:
            t = ListNode()
            t.val = carry
            temp.next = t     
        
        head = head.next
        return head
        
