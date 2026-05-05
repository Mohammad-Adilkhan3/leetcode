# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt, node, result, end = 0, head, None, None
        while node != None:
            cnt+=1
            end = node
            node = node.next
        if cnt==0 or k%cnt == 0:
            return head
        loop = cnt - (k%cnt)
        node = head
        while loop > 1:
            node = node.next
            loop-=1
        result = node.next
        node.next = None
        end.next = head
        return result
