# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr,Next=None,head,head
        if head==None:return None
        while curr:
            Next=curr.next
            curr.next=prev
            prev=curr
            curr=Next
        return prev
        
        