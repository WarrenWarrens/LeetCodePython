class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        else:
            dummy = ListNode()
            curr = head
            while curr != None:
                next_node = curr.next
                prev = dummy

                while prev.next != None and prev.next.val < curr.val:
                    prev = prev.next

                curr.next = prev.next
                prev.next = curr

                curr = next_node

            return dummy.next

    def list_to_linkedlist(arr):
        dummy = ListNode()
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    def linkedlist_to_list(head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr


