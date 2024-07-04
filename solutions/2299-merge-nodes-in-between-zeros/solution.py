# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        dummy = ListNode(0)
        curr = dummy
        temp = 0
        
        while head:
            if head.val == 0:
                if temp!= 0:
                    curr.next = ListNode(temp)
                    curr = curr.next
                    temp = 0
            else:
                temp += head.val
            head = head.next
        
        return dummy.next
        
