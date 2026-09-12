# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_output = ListNode(0, None)
        head = curr_output
        l1_idx = l1
        l2_idx = l2
        continue_for = -1
        last_carry = False
        i = 0

        while l1_idx and l2_idx:
            s = l1_idx.val + l2_idx.val
            curr_output.val += s % 10
            carry = 1 if s>9 else 0
            print("C", curr_output.val)

            l1_idx = l1_idx.next
            l2_idx = l2_idx.next
            if carry == 1:
                curr_output.next = ListNode(carry, None)
                curr_output = curr_output.next
                last_carry = True

            if l1_idx is None:
                if l2_idx is None:
                    continue_for = 0
                continue_for = 2
            elif l2_idx is None:
                continue_for = 1
            elif carry == 0:
                curr_output.next = ListNode(carry, None)
                curr_output = curr_output.next
                last_carry = False
        
        if continue_for == 0:
            return head

        use = l1_idx
        print("1")
        if continue_for == 2:
            use = l2_idx
            print("2")
        print(last_carry)
        while use and i<9:
            i += 1
            if not last_carry:
                curr_output.next = ListNode(0, None)
                curr_output = curr_output.next
            s = curr_output.val + use.val
            curr_output.val = (s) % 10
            if use.next is not None or s>9:
                curr_output.next = ListNode(1 if s>9 else 0, None)
                curr_output = curr_output.next
            use = use.next
        
        return head
        
        

        