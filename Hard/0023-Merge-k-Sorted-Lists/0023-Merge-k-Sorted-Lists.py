# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        head_final = None
        current = None

        for lista in lists:
            if lista:
                heapq.heappush(heap, (lista.val, id(lista), lista))

        while heap:

            val, _, node = heapq.heappop(heap)

            if head_final is None:
                head_final = node
                current = head_final
            else:
                current.next = node
                current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, id(node), node.next))

        return head_final

