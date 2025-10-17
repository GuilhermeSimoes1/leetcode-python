# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        currA = headA
        lenA = 0
        while currA.next:
            lenA += 1
            currA = currA.next

        currB = headB
        lenB = 0
        while currB.next:
            lenB += 1
            currB = currB.next

        if lenB > lenA:

            currA = headA
            currB = headB

            while lenB > lenA:
                lenB -= 1
                currB = currB.next

            while currA != currB:
                currA = currA.next
                currB = currB.next

            return currA

        else:

            currA = headA
            currB = headB

            while lenB < lenA:
                lenA -= 1
                currA = currA.next

            while currA != currB:
                currA = currA.next
                currB = currB.next

            return currA

