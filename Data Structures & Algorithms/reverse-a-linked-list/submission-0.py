# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tailNode = ListNode(0, None)

        while head:
            tailNode.val = head.val
            newNode = ListNode(0, tailNode)
            tailNode = newNode

            head = head.next
        return tailNode.next