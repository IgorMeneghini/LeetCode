# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = 0
        output = ListNode()
        index = output
        while l1 is not None or l2 is not None:
            if l1 is None:
                index.val = (l2.val + temp) % 10
                temp = (l2.val + temp) // 10 if l2 else 0
                l2 = l2.next
            elif l2 is None:
                index.val = (l1.val + temp) % 10
                temp = (l1.val + temp) // 10 if l1 else 0
                l1 = l1.next
            else:
                index.val = (l1.val + l2.val + temp) % 10
                temp = (l1.val + l2.val + temp) // 10
                l1 = l1.next
                l2 = l2.next

            if l1 is not None or l2 is not None:
                index.next = ListNode()
                index = index.next
        if temp != 0:
            index.next = ListNode(temp)
        
        return output