# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            total = x+y+carry
            digit = total%10
            carry = total//10
            curr.next= ListNode(digit)
            curr = curr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next    
