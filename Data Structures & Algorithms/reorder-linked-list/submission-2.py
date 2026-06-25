# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find halves so you can reverse second half
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast is None:
            sh_head = slow
        else:
            sh_head = slow.next
        sh_tail = sh_head.next
        sh_head.next = None
        # Reverse all nodes after this one
        while sh_tail:
            sh_tail_n = sh_tail.next
            sh_tail.next = sh_head
            sh_head = sh_tail
            if sh_tail_n:
                sh_tail = sh_tail_n
            else:
                break
        sh_head = sh_tail

        h1 = head
        h2 = sh_head

        while h2 and h2.next:
            h1_n = h1.next
            h2_n = h2.next

            h2.next = h1_n
            h1.next = h2

            h1 = h1_n
            h2 = h2_n
        
        