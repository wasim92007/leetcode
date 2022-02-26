# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        ## Solution without using any extra memory
        ## We will be using a fast and a slow pointer to
        ## find the middle of the linked list
        slow, fast = head, head
        
        ## The fast pointer is moving twice as fast as the
        ## slow pointer, when the fast pointer is the end
        ## node the slow pointer will point to the middle
        ## of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            

        ## At this point in time the slow pointer will point
        ## to the middle of the linked list
        ## Let us reverse the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        ## prev will contain the reversed slow linked list    
        ## Now we will compare the value as in the array solution
        while prev:
            ## We wil return False if we find mismatch
            if prev.val != head.val:
                return False
            
            ## Update the pointers
            prev = prev.next
            head = head.next
        
        return True
            
        
        
        ## Array solution using extra memory
        arr = []
        
        ## Fill up the values in the arr
        while head:
            arr.append(head.val)
            head = head.next
            
        ## Initialize two pointer    
        i, j = 0, len(arr) - 1

        ## Check for palindrome
        while i <= j:
            ## Check for mismatch
            if arr[i] != arr[j]:
                return False
            i, j = i + 1, j -1
            
        return True
