# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        # Step 1: find the middle using slow/fast pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse the second half, starting right after slow
        second_half = self.reverse(slow.next)
        
        # Step 3: compare first half with reversed second half
        first_half = head
        result = True
        p1, p2 = first_half, second_half
        while p2:
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next
        
        # Step 4 (optional): restore the list by reversing back
        slow.next = self.reverse(second_half)
        
        return result

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev