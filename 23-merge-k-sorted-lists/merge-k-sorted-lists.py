# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        a=[]
        for i in range (len(lists)):
            curr=lists[i]
            while curr:
                heapq.heappush(a,curr.val)
                curr=curr.next
        out=ListNode(0)
        curr=out
        while a:
            val=heapq.heappop(a)
            curr.next=ListNode(val)
            curr=curr.next
        return out.next
        # out=[]
        # for i in range (len(a)):
        #     out.append(heapq.heappop(a))
        # return out