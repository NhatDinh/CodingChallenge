class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        seen = set()
        while (head != None):
            if head in seen:
                return True
            else:
                seen.add(head)
            head = head.next
        return False