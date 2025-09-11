# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        used = []

        current = head

        while current:
            if current not in used:
                used.append(current)
                current = current.next
            else:
                return True
        return False
