# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        count=0
        while curr!=None: 
            count+=1
            curr=curr.next
        if (count%2==1):
            mid=(count+1)//2
        else:
            mid=(count//2)+1
        new=head
        for i in range (mid-1):
            new=new.next
        return new