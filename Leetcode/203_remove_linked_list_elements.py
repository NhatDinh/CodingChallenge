# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
    # Definition for singly-linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        curr = head

        prev = ListNode(-1)
        prev.next = head

        while curr != None:
            if curr is head and curr.val == val:
                head = curr.next
            if curr.val == val:
                prev.next = curr.next
                curr = prev
            prev = curr
            curr = curr.next
        return head
