# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return
        s=set(nums)
        dummy=ListNode(0)
        res=dummy
        while head:
            if head.val not in s:
                dummy.next=head
                head=head.next
                dummy=dummy.next
                dummy.next=None
            else:
                head=head.next
        return res.next

            