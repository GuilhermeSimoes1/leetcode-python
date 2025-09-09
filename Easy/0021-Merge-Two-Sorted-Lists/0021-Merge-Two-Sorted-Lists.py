from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = tail = list1
            curr1 = list1.next
            curr2 = list2
        else:
            head = tail = list2
            curr1 = list1
            curr2 = list2.next

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                tail = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = curr2
                curr2 = curr2.next


        tail.next = curr1 if curr1 else curr2

        return head










