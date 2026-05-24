# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # step 1: find middle node
        l1 = head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: split linked list and reverse l2
        curr = slow.next
        slow.next = None
        prev = None
        
        # step 3: reverse l2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # second half is now reversed with l2 as the
        # head (last element in original linked list)
        l2 = prev

        # step 4: merge the linked lists together
        while l2:
            tmp_l1 = l1.next
            tmp_l2 = l2.next

            l1.next = l2
            l2.next = tmp_l1

            l1 = tmp_l1
            l2 = tmp_l2