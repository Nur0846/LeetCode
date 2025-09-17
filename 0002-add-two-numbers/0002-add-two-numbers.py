# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()         # dummy node to make life easier
        curr, carry = dummy, 0     # curr builds the result list, carry stores overflow

        while l1 or l2 or carry:   # keep going until both lists and carry are done
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry   # add digits + carry
            carry, val = divmod(total, 10)  # split into carry and digit

            curr.next = ListNode(val)  # make new node for result
            curr = curr.next           # move forward

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
