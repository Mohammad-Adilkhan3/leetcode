# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t1 = head   
        t2 = head.next
        current_sum = 0       
        while t2:
            if t2.val == 0:
                t1.val = current_sum
                current_sum = 0
                if t2.next:
                    t1 = t1.next
                else:
                    t1.next = None
            else:
                current_sum += t2.val         
            t2 = t2.next   
        return head
        
