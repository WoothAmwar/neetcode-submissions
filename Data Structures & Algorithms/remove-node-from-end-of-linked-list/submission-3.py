# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r_len = 0
        h = head
        while h:
            h = h.next
            r_len += 1
        # r_len = r_len-1

        h = head
        idx = r_len - n
        curr_idx = 0
        print(r_len, n, h.val)
        while head:
            if idx == 0:
                return h.next
            if curr_idx == idx-1:
                head_n = head.next.next
                head.next = head_n
                return h
            else:
                head = head.next
                curr_idx += 1