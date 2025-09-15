# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Step 1: Put first node of each list into heap
        for i, node in enumerate(lists):
            if node:
                # (value, index, node) -> index ensures no comparison error
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        # Step 2: Process heap until empty
        while heap:
            val, i, node = heapq.heappop(heap)  # get smallest node
            current.next = node                 # attach to result
            current = current.next
            if node.next:                       # push next node of same list
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
