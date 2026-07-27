# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr and curr.next:
            a=curr.val
            b=curr.next.val
            while b!=0:
                a,b=b,a%b
            newnode=ListNode(a)
            temp=curr.next
            curr.next=newnode
            newnode.next=temp
            curr=curr.next.next
        return head