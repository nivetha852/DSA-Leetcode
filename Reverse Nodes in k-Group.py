# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def ishead(node,k):
            count =0
            while node and count<k:
                node = node.next
                count = count+1
            return count == k
        dummy = ListNode(0)
        dummy.next = head
        groupprev = dummy
        while True:
            if not ishead(groupprev.next,k):
                break
            prev,curr = None,groupprev.next
            groupstart = curr
            for _ in range(k):
                nxt = curr.next
                curr.next= prev
                prev = curr
                curr = nxt
                tail = groupprev.next
            groupprev.next = prev
            groupstart.next = curr
            groupprev = groupstart
        return dummy.next
            
        